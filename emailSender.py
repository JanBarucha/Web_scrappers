import os

from redmail import outlook
from dotenv import load_dotenv

_ = load_dotenv()

outlook.username = os.environ.get("EMAIL_ADDRESS")
outlook.password = os.environ.get("EMAIL_PASSWORD")

def send_notification_mail(url):
    outlook.send(
        receivers=['jan.barucha@outlook.com'],
        subject='Promka na Kubku',
        text= 'Link do stronki : ' + url
    )