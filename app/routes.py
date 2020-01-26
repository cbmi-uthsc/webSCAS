from flask import render_template, redirect, url_for, flash, request
from app.forms import PatientForm, SepsisForm
from app.models import Patient, Sepsis
from app import app, db
import flask_whooshalchemy as wa

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
            flash('Your data has been saved successfully', 'success')
            return redirect(url_for('index'))
    return render_template('add_patient.html',title='Add Patient', form=form)

@app.route('/patient_details', methods=['GET', 'POST'])
def patient_details():
    form = SepsisForm()
    if request.method == 'GET':
        return render_template('patient_details.html', title='Patient Details', form=form)
    elif form.validate_on_submit():
        patient_id = Patient.query.filter_by(patient_id=form.patient_id.data).first()
        if patient_id: 
            s_id = Sepsis.query.filter_by(patient_id=form.patient_id.data).first()
            if not s_id:
                details = Sepsis(fever=form.fever.data, heart_rate=form.heart_rate.data, respiratory_rate=form.respiratory_rate.data, abnormal_white_blood_cell_count=form.abnormal_white_blood_cell_count.data, paco2=form.paco2.data, patient_id=form.patient_id.data)
                db.session.add(details)
                db.session.commit()
                flash('Details has been saved', 'success')
            else:
                s_id.fever=form.fever.data
                s_id.heart_rate=form.heart_rate.data
                s_id.respiratory_rate=form.respiratory_rate.data
                s_id.abnormal_white_blood_cell_count=form.abnormal_white_blood_cell_count.data
                s_id.paco2=form.paco2.data
                db.session.commit()
                flash("Details has been updated", 'success')
        else:
            flash('No Patient exist with Patient ID {}'.format(form.patient_id.data), 'warning')
    return render_template('patient_details.html', title='Patient Details', form=form)

# @app.route('/search')
# def search():
#     data = request.args.get('query')
#     # print(data)
#     patients = Patient.query.whoosh_search(data).all()
#     print(type(patients))
#     return render_template('index.html', patients=patients)
#     # return 'hi'