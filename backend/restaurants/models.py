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

    class Meta:
        verbose_name="Coordinates"
        verbose_name_plural="Coordinates"


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


class Review(TimeStamp):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_reviews"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_reviews'
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.user.name}'s review on {self.restaurant.name}"


class Icon(models.Model):
    icon = models.CharField(
        max_length=100
    )
    name = models.CharField(
        max_length=250,
        help_text="Numele care apare pe ecran"
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class Tips(models.Model):
    icon = models.ForeignKey(
        Icon,
        on_delete=models.CASCADE,
    )
    color = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.icon.name

    class Meta:
        verbose_name = "Tip"
        verbose_name_plural = "Tips"

    
class Badge(models.Model):
    icon = models.ForeignKey(
        Icon,
        on_delete=models.CASCADE,
    )
    color = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.icon.name



class RestaurantBadge(models.Model):
    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE,
        related_name="restaurant_badges"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant.name}'s badge ({self.badge.icon.name})"


class UserBadge(models.Model):
    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE,
        related_name="user_badges"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s badge ({self.badge.icon.name})"

    class Meta:
        app_label = 'accounts'


class UserRestaurants(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_restaurants"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s restaurant ({self.restaurant.name})"

    class Meta:
        app_label = 'accounts'


class MenuTypes(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Product(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_products'
    )
    type = models.ForeignKey(
        MenuTypes,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    ingredients = models.TextField()

    def __str__(self):
        return f"{self.name} for {self.restaurant.name}"


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_images"
    )
    image = models.ImageField(upload_to=settings.MEDIA_ROOT + '/restaurants/products')

    def __str__(self):
        return f"{self.product.name}'s image"

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'



# class Menu(models.Model):
#     restaurant = models.ForeignKey(
#         Restaurant,
#         on_delete=models.CASCADE,
#         related_name='restaurant_menus'
#     )

#     def __str__(self):
#         return f"{self.restaurant.name}'s menu"

# Todo
# class Product(models.Model):
#     menu = models.ForeignKey(
#         Menu,
#         on_delete=models.CASCADE,
#         related_name="menu_products"
#     )
#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )



    


    

