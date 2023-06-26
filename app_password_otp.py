from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'latuamail@gmail.com'  # Aggiungi il tuo indirizzo email
app.config['MAIL_PASSWORD'] = 'latuapassword'  # Aggiungi la tua password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

otp_code = None

@app.route('/', methods=['GET', 'POST'])
def login():
    global otp_code

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'latuamail@gmail.com' and password == '1234':
            otp_code = generate_otp_code()
            send_otp_email(username, otp_code)
            return redirect(url_for('verify_otp'))
        else:
            return render_template('log.html', error='Credenziali non valide.')

    return render_template('log.html')

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    global otp_code

    if request.method == 'POST':
        entered_otp = request.form['otp']

        if entered_otp == otp_code:
            otp_code = None  # Reset del codice OTP
            return render_template('success.html')
        else:
            return render_template('verify_otp.html', error='Codice OTP non valido.')

    return render_template('verify_otp.html')

def generate_otp_code():
    return str(random.randint(100000, 999999))

def send_otp_email(recipient, otp_code):
    msg = Message('Codice OTP', sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.body = f'Il tuo codice OTP è: {otp_code}'
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)

