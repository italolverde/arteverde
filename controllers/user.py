from flask import Blueprint, request, render_template, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, UserMixin, LoginManager, current_user
import sqlite3

from db.db import TB_User, session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return TB_User.find(id=user_id)

bp_user = Blueprint('user', __name__, url_prefix='/user', template_folder='../templates/users')

def get_connection():
    conn = sqlite3.connect("../banco.db")
    conn.row_factory = sqlite3.Row
    return conn

@bp_user.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])
        admin = False #LEMBRAR DE MUDAR ISSO DEPOIS

        users = session.query(TB_User).all()
        for user in users:
            if email == user.email:
                flash('Esse email ja está cadastrado.','error')
                return redirect(url_for('user.register'))
        #SE O EMAIL NÃO FOR REPETIDO
        novo_user = TB_User(nome=nome,email=email,senha=senha,admin=admin)
        session.add(novo_user)
        session.commit()
        flash('Usuário cadastrado com sucesso','sucess')
        return redirect(url_for('home'))
    return render_template('register.html')

@bp_user.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = session.query(TB_User).filter(TB_User.email == email).first()   
        if not usuario:
            flash('Email não encontrado')
            print('------------ email não encontrado')
            return redirect(url_for('user.login'))
        else:
            if check_password_hash(usuario.senha,senha):
                print('---------------- Login bem sucedido')
                flash('Login bem sucedido')
                login_user(usuario)
                usuario = current_user
                return redirect(url_for('home'))
                
            else:
                flash('Senha incorreta')
                print('-------------------------------- Senha incorreta')
                return render_template('login.html',email=email)
    return render_template('login.html')

@bp_user.route('/logout', methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))

# @bp_user.route('/flash_message')
# def flash_message():
#     flash('Esse email ja está cadastrado.')