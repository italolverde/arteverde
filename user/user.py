from flask import Blueprint, request, render_template, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
import sqlite3
from db.db import TB_User

login_manager = LoginManager()

bp_user = Blueprint('user', __name__, url_prefix='/user')

def get_connection():
    conn = sqlite3.connect("../banco.db")
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self,nome,email,senha,admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
    

@bp_user.route('/register')
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = generate_password_hash(request.form['senha'])
    admin = False #LEMBRAR DE MUDAR ISSO DEPOIS

    conn = get_connection()
    users = conn.execute('SELECT * FROM users')
    for user in users:
        if email == user[email]:
            flash('Esse email ja está cadastrado.')
            return redirect(url_for('/user/register'))
        else:
            novo_user = User(nome,email,senha,admin)
            TB_User(novo_user)
            session['user'] = novo_user


# @bp_user.route('/flash_message')
# def flash_message():
#     flash('Esse email ja está cadastrado.')