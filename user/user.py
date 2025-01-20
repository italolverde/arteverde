from flask import Blueprint, request, render_template, session, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
import sqlite3

from db.db import TB_User, session

login_manager = LoginManager()

bp_user = Blueprint('user', __name__, url_prefix='/user', template_folder='./templates')

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
    

@bp_user.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])
        admin = False #LEMBRAR DE MUDAR ISSO DEPOIS

        conn = get_connection()
        users = session.query(TB_User).all()
        for user in users:
            if email == user.email:
                flash('Esse email ja está cadastrado.')
                return redirect(url_for('user.register'))
            else:
                novo_user = TB_User(nome,email,senha,admin)
                session.add(novo_user)
                session.commit()
    return render_template('register.html')


# @bp_user.route('/flash_message')
# def flash_message():
#     flash('Esse email ja está cadastrado.')