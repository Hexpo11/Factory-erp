from django.db import models  # type: ignore
from django.conf import settings  # type: ignore


class AuditLog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	action = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)