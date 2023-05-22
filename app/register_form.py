from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    block = StringField('Bloque', validators=[DataRequired()])
    apartment = StringField('Apartamento', validators=[DataRequired()])
    owner_name = StringField('Nombre de Propietario', validators=[DataRequired()])
    tenant_name = StringField('Nombre de Arrendatario', validators=[DataRequired()])
    type_vehicles = StringField('Tipo de vehiculo', validators=[DataRequired()])
    vehicle_reference = StringField('Referencia del vehiculo', validators=[DataRequired()])
    plate = StringField('Placa del vehiculo', validators=[DataRequired()])
    submit = SubmitField('Registrar')