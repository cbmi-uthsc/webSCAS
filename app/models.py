from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    patient_name = db.Column(db.String(64), index=1)
    patient_id = db.Column(db.String(64), index=1)
    patient_disease = db.Column(db.String(128), index=1)

    def __repr__(self):
        return '<Patient {}>'.format(self.patient_id)

# def load_user(id):
#     return User.query.get(int(id))