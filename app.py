import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'MAIL_USERNAME'
app.config['MAIL_PASSWORD'] = 'MAIL_PASSWORD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    # return render_template('index.htnl')
    msg = Message('', sender = 'MAIL_USERNAME', recipients = ['', ''])
    
    msg.subject = 'Follow-up'

    # msg.body = 'Hi there!,\n\nThank you for visiting ...! I hope this message finds you well.\nI would be very glad to hear more about your interest, whether for a collaboration, for hiring, or for enrolling to one of my classes.\nKing regards,\nBot'
    # msg.html = '''
    # <div style = 'width: 50vw; height: 50vh; border: solid silver 0.2px; border-radius: 1em; position: relative; left: 50%; transform: translate(-50%);'>
    #     <h1 style='color:rgb(42, 165, 81); display: flex; justify-content: center; text-align: center; align-items: center; height: 100%; margin: 0;'>
    #         Thank you for visiting!
    #     </h1>
    # </div>
    # '''
    mail.send(msg)
    return "Sent"

