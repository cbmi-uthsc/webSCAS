from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PatientForm(FlaskForm):
    patient_id = StringField('Patient Id', validators=[DataRequired()])
    patient_name = StringField('Patient Name', validators=[DataRequired()])
    patient_disease = StringField('Disease', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SepsisForm(FlaskForm):
    patient_id = StringField('Patient ID', validators=[DataRequired()])
    fever = StringField('Fever(in degree celsius)', validators=[DataRequired()])
    heart_rate = StringField('Heart Rate(in beats per minute)', validators=[DataRequired()])
    respiratory_rate = StringField('Respiratory Rate(in breaths per minute)', validators=[DataRequired()])
    abnormal_white_blood_cell_count = StringField('Abnormal White Blood Cell Count(/mm3)', validators=[DataRequired()])
    paco2 = StringField('PaCO2(Partial pressure of carbon dioxide)')
    submit = SubmitField('Submit')
