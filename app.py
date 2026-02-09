from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

import json
app = Flask(__name__)

db = SQLAlchemy()

db_name = 'pi2025_nexo'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

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
