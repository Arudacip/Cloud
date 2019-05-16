import os

from flask import Flask, render_template, request
from flask_sockets import Sockets
from jsonConverter import convertToJson

from DataBase.DataAccess.MySQL.MySQLDB import mySQL

from Model.texto import texto
from Model.model import model

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
    banco = mySQL()
    banco.autoCommit = True
    banco.execModQuery("INSERT INTO Teste VALUES (0)")
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
    return convertToJson(HelloWorld="Hello World! Retorno em JSON da API de testes!")


@app.route('/game', methods=['GET'])
def game_start():
    '''
        Requisição para iniciar o game
    '''
    model = texto("", "", 1)
    return render_template('game.html', isStart=True, model=model)

@app.route('/game', methods=['POST'])
def game_post():
    '''
        Requisição para iniciar o game
    '''
    jogo = game()
    #if(request.form.get('isStart') is not None):
    #    Modelo = jogo.firstPost()
    #else:
    Modelo = jogo.notFirstPost()
    
    if(Modelo is not None):
        return render_template('game.html', model=Modelo)
    else:
        return render_template('errorNotImplemented.html')
@app.route('/game/visualizer')
def game_visualizer():
    '''
        Visualizar do grafo do jogo
    '''
    return render_template('visualizer/index.html')


'''@app.route('/api/<path:path>', methods=['GET']) #Impede que a API seja acessa por browser
def error_OnlyPost():
    return render_template('errorOnlyPost.html')'''

if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port=5050)

#Teste
