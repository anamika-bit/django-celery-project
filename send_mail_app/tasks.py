from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celery_project import settings

@shared_task(bind = True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    to_email = []
    for user in users:
        mail_subject = 'Hi, celery Testing'
        message = 'If u are liking my content , please hit the like button and do subscribe my channel.'
        to_email.append(user.email)

    send_mail(
        subject = mail_subject, 
        message = message, 
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = to_email,
        fail_silently = False
    )
        
    return "Done"