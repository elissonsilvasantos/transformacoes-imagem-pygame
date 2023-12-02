from __future__ import print_function # In python 2.7
import sys

from flask import Flask, render_template

from flask import request




name = 'main'
app = Flask(name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rotacionar')
def rotacionar():
    # Lógica para a operação de rotação
    return "Executando a operação de rotação..."

@app.route('/transladar')
def transladar():
    # Lógica para a operação de translação
    #print('Hello world!', file=sys.stderr)
    return "Executando a operação de translação..."

@app.route('/mover')
def mover():
    # Lógica para a operação de mover
    return "Executando a operação de mover..."

@app.route('/escolher_imagem')
def escolher_imagem():
    # Lógica para escolher a imagem
    return "Escolhendo a imagem..."

def teste():
    request.path

if name == 'main':
    app.run(debug=True)
