from django.contrib.auth.models import User
from django.db import models


class Conversion(models.Model):
    input_number = models.BigIntegerField()
    output_words = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.input_number} - {self.output_words}"
