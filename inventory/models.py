from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    min_quantity = models.IntegerField()

    # 🔹 REQUIRED for low stock email logic
    low_stock_alert_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name
