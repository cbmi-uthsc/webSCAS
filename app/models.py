from app import db, app
import flask_whooshalchemy as wa

class Patient(db.Model):
    # id = db.Column(db.Integer, primary_key=1)
    __searchable__ = ['patien_name', 'patient_disease']
    patient_id = db.Column(db.Integer, primary_key=1)
    patient_name = db.Column(db.String(64))
    patient_disease = db.Column(db.String(128))
    sepsis = db.relationship('Sepsis', backref='patient', lazy='dynamic')

    def __repr__(self):
        return '<Patient {}>'.format(self.patient_id)
    
wa.whoosh_index(app, Patient)
class Sepsis(db.Model):
    s_id = db.Column(db.Integer, primary_key=1)
    fever = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    respiratory_rate = db.Column(db.Integer)
    abnormal_white_blood_cell_count = db.Column(db.Integer)
    paco2 = db.Column(db.Integer)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

# def load_user(id):
#     return User.query.get(int(id))