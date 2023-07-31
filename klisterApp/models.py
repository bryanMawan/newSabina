from django.db import models

# Create your models here.

stadsdelar = [("Stadsområde Centrum", "Stadsområde Centrum"), ("Stadsområde Nordost", "Stadsområde Nordost"), ("Stadsområde Sydväst", "Stadsområde Sydväst"), ("Stadsområde Hisingen", "Stadsområde Hisingen")]


class formPage(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    stadsdel = models.CharField(max_length=21, choices=stadsdelar)
    idrott = models.CharField(max_length=100)
    önskad_idrott = models.CharField(max_length=100, verbose_name="Önskad idrott")
    in_a_union = models.BooleanField()
    filePath = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class password(models.Model):
    password = models.CharField(max_length=100)


class SpreadsheetId(models.Model):
    IDString = models.CharField(max_length=1024)
    gid = models.CharField(max_length=1024)