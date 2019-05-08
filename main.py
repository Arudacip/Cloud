import os

from flask import Flask, render_template, request
from flask_sockets import Sockets
from jsonConverter import convertToJson

from Model.texto import texto
from Model.model import model

from Processing.game import game

#Hello World
app = Flask(__name__)
app.debug = 'DEBUG' in os.environ
sockets = Sockets(app)

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
    return render_template('game.html', isStart=True)

@app.route('/game', methods=['POST'])
def game_post():
    '''
        Requisição para iniciar o game
    '''
    jogo = game()
    if(request.form.get('isStart') is not None):
        Modelo = jogo.firstPost()
    else:
        Modelo = jogo.notFirstPost()
    
    return render_template('game.html', model=Modelo)

'''@app.route('/api/<path:path>', methods=['GET']) #Impede que a API seja acessa por browser
def error_OnlyPost():
    return render_template('errorOnlyPost.html')'''

if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port=5050)



