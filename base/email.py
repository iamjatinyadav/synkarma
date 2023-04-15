from django.core.mail import send_mail
from django.conf import settings


def send_successfully_email(email, message):
    subject = "Your Post Create SuccessFully"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])