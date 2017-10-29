from django.contrib import admin

# Register your models here.
from .models import Kunden, Referanten

admin.site.register(Kunden)
admin.site.register(Referanten)