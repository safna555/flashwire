from django.db import models

class Cracker(models.Model):
    name = models.CharField(max_length=100, unique=True)  # prevent duplicate names
    description = models.TextField(blank=True)  # optional description
    image = models.ImageField(upload_to='crackers/', blank=True, null=True)  # allow empty images
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    discount = models.PositiveIntegerField(default=0)  # discount in %
    image = models.ImageField(upload_to='offers/', blank=True, null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    userid = models.AutoField(primary_key=True)  # auto increment ID
    phone = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return f"{self.username} ({self.userid})"



