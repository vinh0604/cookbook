from email.mime.text import MIMEText
import smtplib

class SMTPClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, from_email, to, subject, body):
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = from_email
        message['To'] = to

        with smtplib.SMTP(self.host, self.port) as server:
            server.login(self.username, self.password)
            server.sendmail(from_email, to, message.as_string())