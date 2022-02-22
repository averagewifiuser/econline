from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SubmitField)
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Admin



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    
class NewAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    def validate_username(self, email):
        user = Admin.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is not available')

