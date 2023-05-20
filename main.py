from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

data_user = ['bloque', 'apartamento', 'nom_propietario']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/home'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/home')
def home():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'data_user' : data_user,
    }

    return render_template('base.html', **context)