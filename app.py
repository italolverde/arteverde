from flask import Flask, render_template
from user.user import bp_user
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'asdfghjklñ'
app.register_blueprint(bp_user)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')
    