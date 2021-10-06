from django.core.mail import get_connection
from django.conf import settings
from config.celery import app


@app.task(rety_backoff=False, serializer="pickle")
def async_send_messages(email_messages):
    conn = get_connection(
        backend='django.core.mail.backends.smtp.EmailBackend',
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS
    )
    conn.send_messages(email_messages)
