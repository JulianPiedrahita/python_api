import unittest

from flask import Flask, request, make_response, \
     redirect, render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

app.config['SECRET-KEY'] = 'SUPER SECRETO'
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(test)

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
    }

    return render_template('base.html', **context)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user_ip = session.get('user_ip')
    register_form = RegisterForm()
    owner_name = session.get('owner_name')

    context = {
        'user_ip': user_ip,
        'owner_name': owner_name,
        'register_form': register_form,
    }

    if register_form.validate_on_submit():
        owner_name = register_form.owner_name.data
        session['owner_name'] = owner_name

        flash('Usuario registrado con exito!')

        return redirect(url_for('home'))

    return render_template('register.html', **context)

class RegisterForm(FlaskForm):
    block = StringField('Bloque', validators=[DataRequired()])
    apartment = StringField('Apartamento', validators=[DataRequired()])
    owner_name = StringField('Nombre de Propietario', validators=[DataRequired()])
    tenant_name = StringField('Nombre de Arrendatario', validators=[DataRequired()])
    type_vehicles = StringField('Tipo de vehiculo', validators=[DataRequired()])
    vehicle_reference = StringField('Referencia del vehiculo', validators=[DataRequired()])
    plate = StringField('Placa del vehiculo', validators=[DataRequired()])
    submit = SubmitField('Registrar')