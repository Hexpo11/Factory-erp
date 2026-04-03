from django.core.mail import send_mail
from django.conf import settings

def send_low_stock_email(material):
    send_mail(
        subject=f"⚠️ Low Stock Alert: {material.name}",
        message=(
            f"Material: {material.name}\n"
            f"Current Quantity: {material.quantity}\n"
            f"Minimum Required: {material.min_quantity}\n\n"
            "Please restock immediately."
        ),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
