from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PatientForm(FlaskForm):
    patient_name = StringField('Patient Name', validators=[DataRequired()])
    patient_id = StringField('patient Id', validators=[DataRequired()])
    patient_disease = StringField('Disease', validators=[DataRequired()])
    submit = SubmitField('Submit')