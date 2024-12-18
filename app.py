from flask import Flask, render_template
from user.user import bp_user

app = Flask(__name__)

app.register_blueprint(bp_user)

@app.route('/')
def index():
    return render_template('index.html')
    