from django.db import models

class QuoteRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    services = models.CharField(max_length=255)
    project_size = models.CharField(max_length=50, blank=True)
    timeline = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"