from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from .email import *


@receiver(post_save, sender= Post)
def make_cart(sender, instance, created,  **kwargs):
    if instance.title:
        email = (instance.author.email)
        body = (instance.body)
        send_successfully_email(email, body)
