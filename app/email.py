from flask_mail import Message
from app import mail

def send_email(recipient, subject, body):
    try:
        msg = Message(subject, recipients=[recipient], body=body)
        mail.send(msg)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")