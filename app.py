import os
from flask import Flask, render_template, jsonify, request, url_for, redirect, flash
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(
    __name__
)
CORS(app)

app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)

@app.route('/testmail', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient = request.form['recipient']
        msg = Message('Twilio SendGrid Test Email 2', recipients=[recipient])
        msg.body = ('Congratulations! You have sent a test email with '
                    'Twilio SendGrid!')
        msg.html = ('<h1>Twilio SendGrid Test Email</h1>'
                    '<p>Congratulations! You have sent a test email with '
                    '<b>Twilio SendGrid</b>!</p>')
        msg.reply_to = 'rivkekilmer@gmail.com'
        mail.send(msg)
        flash(f'A test message was sent to {recipient}.')
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/form/contact', methods=['POST', 'GET'])
def contactform():
    print(request.get_json())
    details = request.get_json()
    phone_to_bust_spam = details['phone']
    if phone_to_bust_spam != '8882221111':
        return jsonify({'error': 'You are a spammer!'})
    name = details['name']
    email = details['email']
    message = details['message']
    msg = Message(f'Contact PageFlow', recipients=['support@pageflow.com','john@pageflow.com'])
    msg.body = f'{name} ({email}) sends: {message}'
    msg.reply_to = email
    mail.send(msg)
    return jsonify({'success': 'Message sent!'})

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
