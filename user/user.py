from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
import sqlite3

##

login_manager = LoginManager()
app.config['SECRET_KEY'] = 'CHAVE'
login_manager.init_app(app)

##

def get_connection():
    conn = sqlite3.connect("../banco.db")
    conn.row_factory = sqlite3.Row
    return conn

##

class User(UserMixin)
    def __init__(self,email,nome,senha):
        self.email = email
        self.nome = nome
        self.senha = senha
    
    @classmethod
    def get_by_email(cls, email):
        conn = get_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?',(email))
        return user