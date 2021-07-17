from flask_wtf import FlaskForm
from boot_flask.models import Subscriber
from wtforms import StringField, SubmitField, TextAreaField,TextField
from wtforms.validators import DataRequired,Length, Email, ValidationError

class Contact_Us(FlaskForm):
    name = StringField('Your Name',validators=[DataRequired(), Length(min=4,max=25)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    subject= TextField('Subject',validators=[DataRequired(),Length(min=3,max=200)])
    message = TextAreaField('Message/Query', validators=[DataRequired()])
    submit = SubmitField('Send Message')

class Newsletter(FlaskForm):
    email = StringField('Email',validators= [DataRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,email):
        
        user = Subscriber.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email ID already registered!')   