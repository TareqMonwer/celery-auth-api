import os
from django.core.mail import get_connection
from django.conf import settings
from config.celery import app


@app.task(rety_backoff=False, serializer="pickle")
def async_send_messages(email_messages):
    conn = get_connection(
        backend='django.core.mail.backends.smtp.EmailBackend',
        host=os.environ.get('EMAIL_HOST'),
        port=os.environ.get('EMAIL_PORT'),
        username=os.environ.get('EMAIL_HOST_USER'),
        password=os.environ.get('EMAIL_HOST_PASSWORD'),
        use_tls=True
    )
    conn.send_messages(email_messages)
