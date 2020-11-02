from django.db import models
from django.conf import settings
from accounts.models import User


def upload_to():
    return

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Restaurant(TimeStamp):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class RestaurantImages(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to=settings.MEDIA_ROOT + '/restaurants')

    def __str__(self):
        return f"{self.restaurant.name}'s image #{self.id}"

    class Meta:
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'

class Contact(TimeStamp):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='contact'
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name="Phone number"
    )
    email = models.EmailField()
    address = models.TextField()
    website_url = models.URLField(
        verbose_name="Website"
    )

    def __str__(self):
        return f"{self.restaurant.name}'s contact"


class Coordinates(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='coordinates'
    )
    latitude = models.DecimalField(max_digits=8, decimal_places=4)
    longitude = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
        return f"{self.contact.restaurant.name}'s coordinates"


class Rating(TimeStamp):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    value = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    def __str__(self):
        return f"{self.user.username}'s rating for {self.restaurant.name}"
