from django.db import models

class Cracker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='crackers/')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.PositiveIntegerField()  # discount in percentage
    image = models.ImageField(upload_to='offers/')  # store images in media/offers/

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    userid = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


