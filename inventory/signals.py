from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Material

@receiver(post_save, sender=Material)
def low_stock_email_alert(sender, instance, **kwargs):
    if instance.quantity <= instance.min_quantity and not instance.low_stock_alert_sent:
        send_mail(
            subject="⚠️ Low Stock Alert",
            message=f"Material '{instance.name}' is low on stock.\n\n"
                    f"Current quantity: {instance.quantity}\n"
                    f"Minimum required: {instance.min_quantity}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Mark alert as sent
        instance.low_stock_alert_sent = True
        instance.save(update_fields=["low_stock_alert_sent"])
