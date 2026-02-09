from flask import Flask, render_template
import mysql.connector

import json
app = Flask(__name__)


conexao = mysql.connector.connect(
    host='localhost',
    user='psi2025_maria_07',
    password='maria$#santos', 
    database='pi2025_nexo',
)
cursor = conexao.cursor()

class usuario(db.Model):
    __tablename__ = 'usuario'
    nome_usuario = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(250))
    tipo_usuario = db.Column(db.String(250))
    email = db.Column(db.String)(250)
    telefone= db.Column(db.String(23))
    data_nascimento = db.Column(db.date)
    senha = db.Column(db.String(20))
    endereco = db.Column(db.String(100))
    sexo = db.Column(db.String(1))

class grupo(db.Model):
    __tablename__ = 'grupo'
    id = db.column(db.integer, primary_key = True)
    data_criacao = db.Column(db.date)
    nome = db.Column(db.String(50))
    descricao_grupo = db.Column(db.String(50))
    classificacao_grupo = db.Column(db.integer) 

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/home')
def base ():
    return render_template('home.html')

@app.route('/apresentacao')
def apresentacao ():
    return render_template('apresentacao.html')

@app.route('/cadastro/<cadastro>')
def cadastro (cadastro):
    if cadastro == 'leitor':
        return render_template('cadastro.html', cadastro='leitor')
    else:
        return render_template('cadastro.html', cadastro='autor')
   
@app.route('/grupo')
def grupo ():
    return render_template('grupo.html')

@app.route('/lives')
def lives ():
    return render_template('lives.html')

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/perfil')
def perfil ():
    return render_template('perfil.html')

@app.route('/postagens')
def postagens ():
    return render_template('postagens.html')

@app.route('/sobrenos')
def sobrenos ():
    return render_template('sobrenos.html')

@app.route('/perfil_joao')
def perfil_joao():
    with open('livros_joao.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return render_template('perfil_joao.html', dados=dados)
    
    
if __name__== '__main__':
  app.run()
