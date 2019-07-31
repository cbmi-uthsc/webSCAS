
# Imports
##########

from . import db

###############################################################################


# Base Class
#############

class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def serialize(self, return_fields=[]):
        serialize_exclude = getattr(self, '__serialize_exclude__', set())
        return_fields = self.__dict__.keys() if not return_fields else return_fields
        return {
        	key: value for key, value in self.__dict__.items()
                # Do not serialize 'private' attributes
                # (SQLAlchemy-internal attributes are among those, too)
                if not key.startswith('_')
                and key in return_fields
                and key not in serialize_exclude}

    def create(self):
    	db.session.add(self)
    	db.session.commit()

###############################################################################