from django.core.mail import EmailMessage
from django.conf import settings


def send_contact_email(user_name, user_email, subject, message):
    email_subject = f"New Message from MalangCode Portal of Subject: {subject}"
    email_body = f"""
    Name: {user_name}
    Email: {user_email}
    
    Message:
    {message}
    """

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.SENDER_EMAIL,  # Your sender email
        to=[settings.EMAIL_HOST_USER],  # Your inbox
        reply_to=[user_email],  
    )

    email.send()
