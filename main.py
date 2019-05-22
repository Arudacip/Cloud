import os

from flask import Flask, render_template, request, Response
from flask_sockets import Sockets
from jsonConverter import convertToJson

from DataBase.DataAccess.MySQL.MySQLDB import mySQL

from Model.texto import texto
from Model.model import model

from Model.DB_Models.faseModel import convertFasesToJson

from Processing.game import game

#Hello World
app = Flask(__name__)
app.debug = 'DEBUG' in os.environ
sockets = Sockets(app)

@app.route('/beta/api/testeEnvioBD')
def testeConnexBD():
    '''
        Envia algum dado de teste para o banco de dados
    '''
    banco = mySQL(True)
    banco.execModQuery("INSERT INTO Teste VALUES (0, 0)")
    pass

@app.route('/')
def hello():
    '''
    Retorna uma página de inicio contendo os membros do grupo
    '''
    return render_template('index.html')

@app.route('/api/HelloWorld', methods=['POST', 'GET'])
def api_HelloWorld():
    '''
        Requisição simples de hello world para testar a API
    '''
    return Response(convertToJson(HelloWorld="Hello World! Retorno em JSON da API de testes!"), mimetype='application/json')

@app.route('/api/game/fases', methods=['POST', 'GET'])
def api_Fases():
    '''
        Requisição para retornar o contexto de fases do banco de dados
    '''
    return Response(convertFasesToJson(), mimetype='application/json')


@app.route('/game', methods=['GET'])
def game_start():
    '''
        Requisição para iniciar o game
    '''
    model = texto("", "", 1)
    return render_template('game.html', isStart=True)

@app.route('/game', methods=['POST'])
def game_post():
    '''
        Requisição para iniciar o game
    '''
    jogo = game()
    Modelo = jogo.notFirstPost()
    
    if(Modelo is not None):
        return render_template('game.html', model=Modelo)
    else:
        return render_template('errorNotImplemented.html')

@app.route('/game/<proximaFase>', methods=['POST'])
def game_nextFase(proximaFase):
    '''
        Requisição para ir para a próxima fase
    '''
    jogo = game()
    Modelo = jogo.nextFase(request.form.get('nextFase'))
    
    if(Modelo is not None):
        return render_template('game.html', model=Modelo)
    else:
        return render_template('errorNotImplemented.html')
    pass
        
@app.route('/game/visualizer')
def game_visualizer():
    '''
        Visualizar do grafo do jogo
    '''
    return render_template('visualizer/index.html')

@app.route('/game/visualizer/beta')
def game_visualizerBeta():
    '''
        Visualizar do grafo do jogo
    '''
    return render_template('visualizer/allFases.html', jsonData=convertFasesToJson())

if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port=5050)

#Teste
