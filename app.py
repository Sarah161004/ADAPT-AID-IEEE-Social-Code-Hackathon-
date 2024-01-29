
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/')
def index():
    return redirect(url_for('login'))  # Redirect to login page by default

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Handle registration logic here
        return "Registration successful!"

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Handle login logic here
        return "Login successful!"

    return render_template('login.html', form=form)
 
@app.route('/page2.html')
def page2():
    # Your 2nd page's logic here
    return render_template('page2.html')

@app.route('/page3.html')
def page3():
    # Your 2nd page's logic here
    print("here")
    return render_template('page3.html')

if __name__ == '_main_':
    app.run(debug=True)
    