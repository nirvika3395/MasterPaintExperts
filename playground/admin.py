from django.contrib import admin

# Register your models here.

from .models import QuoteRequest

admin.site.register(QuoteRequest)