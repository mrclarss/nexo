from flask import Flask, render_template
import json

app=Flask(__name__)

@app.route('/')
def index():
    with open('livros_joao.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return render_template('perfil_joao.html', dados=dados)