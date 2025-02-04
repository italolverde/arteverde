from flask import Flask, render_template, url_for, redirect, request
from controllers.user import bp_user, login_manager
from flask_login import LoginManager
from db.db import Base,engine

app = Flask(__name__)
app.secret_key = 'asdfghjklñ'
app.register_blueprint(bp_user)
login_manager.init_app(app)


with app.app_context():
    Base.metadata.create_all(bind=engine)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('homepage.html')




