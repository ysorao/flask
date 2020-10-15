from flask import Flask, render_template, request, redirect, make_response, session, url_for
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, PasswordField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY']='cL4V35ECR3T4'


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Enviar') 





@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error = error) 


@app.route('/')
def index():
    return('Pagina inicial')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    username = session.get('username')

    context = {
        'loginForm': loginForm,
        'username': username,
        'loginForm': loginForm
    }
    
    username = loginForm.username.data
    # session['username'] = username
    # return redirect(url_for('login'))

    return render_template('login.html', **context )


@app.route('/registro')
def registro():
    mensaje = 'Registro de entrada y salida'
    context={
        'mensaje': mensaje,
    }
    return render_template('registro.html', **context)


@app.route('/repIndividual')
def repIndividual():
    return render_template('repIndividual.html')


if __name__ == '__main__':
    app.run(host= 'localhost',  port= 8000, debug = True)