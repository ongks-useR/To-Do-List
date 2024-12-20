from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5

csrf = CSRFProtect()
bootstrap = Bootstrap5()


# New User Registeration
class SignUp(FlaskForm):
    full_name = StringField(label='Full Name:',
                            validators=[InputRequired(), Length(min=3, max=20)],
                            render_kw={'placeholder': 'Full Name'})
    email = EmailField(label='Email:',
                       validators=[InputRequired(), Email(granular_message=True, check_deliverability=True)],
                       render_kw={'placeholder': 'example@gmail.com'})
    password = PasswordField(label='Password:',
                             validators=[InputRequired(), Length(min=8, max=12)],
                             render_kw={'placeholder': '**********'})
    agreement = BooleanField(label='I agree to the Terms & Conditions.',
                             validators=[InputRequired()])
    register = SubmitField(label='Register', id='register-btn')