from flask import render_template, redirect, url_for, flash, request
from app.forms import PatientForm
from app.models import Patient
from app import app, db

@app.route('/')
@app.route('/index')
def index():
    patients = Patient.query.all()
    for patient in patients:
        print(patient.patient_name)
    return render_template("index.html", title="webscas", patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    form = PatientForm()
    if request.method == 'GET':
        return render_template('add_patient.html', title='Add Patient', form=form)
    elif form.validate_on_submit():
        patient_id = Patient.query.filter_by(patient_id=form.patient_id.data).first()
        print(type(patient_id))
        if patient_id is not None:
            flash('Patient with id {} already exist'.format(form.patient_id.data), 'info')
            return redirect(url_for('add_patient'))
        else:
            patient = Patient(patient_name=form.patient_name.data, patient_id=form.patient_id.data, patient_disease=form.patient_disease.data)
            db.session.add(patient)
            db.session.commit()
            flash('Your data has been saved successfulluy', 'success')
            return redirect(url_for('index'))
    return render_template('add_patient.html',title='Add Patient', form=form)
