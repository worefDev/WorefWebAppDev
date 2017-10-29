from django.db import models

# Create your models here.
class Kunden(models.Model):
    Kunden_ID       = models.AutoField(max_length=100,primary_key=True)
    Name            = models.CharField(max_length=100)
    Kommentar       = models.CharField(max_length=1000)
    Actung          = models.BooleanField(default=0,blank=False)
    en              = models.BooleanField(default=0,blank=False)
    Telefon         = models.CharField(max_length=100,null=True, blank=False)
    eMail           = models.CharField(max_length=100)
    Kontoinhaber    = models.CharField(max_length=100)
    Kontonummer     = models.CharField(max_length=100)
    BLZ             = models.CharField(max_length=100,null=True, blank=False)
    Bank            = models.CharField(max_length=100)


class Referanten(models.Model):
    ID              = models.AutoField (max_length=100,primary_key=True)
    EintrittsDatum  = models.DateField(auto_now_add=True)
    Name            = models.CharField(max_length=100)
    Activ           = models.BooleanField(default=0, blank=False)
    Schluessel      = models.BooleanField(default=0, blank=False)

