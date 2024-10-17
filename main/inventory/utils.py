from django.core.mail import send_mail
from django.conf import settings

def send_low_stock_alert(item):
    subject = f"Low Stock Alert: {item.name}"
    message = f"The inventory level for {item.name} has dropped below the threshold.\nCurrent stock: {item.quantity}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['tedibewuket@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
