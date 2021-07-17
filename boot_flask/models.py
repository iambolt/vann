from boot_flask import db
from datetime import datetime

class Queries(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    subject = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Query('{self.name}', '{self.date_posted}', '{self.subject}','{self.message}')"



class Subscriber(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Query('{self.email}')"
     
