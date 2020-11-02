from django.contrib import admin
from .models import (
  Restaurant, 
  RestaurantImages,
  Contact,
  Coordinates,
  Rating
)


admin.site.register(Restaurant)
admin.site.register(RestaurantImages)
admin.site.register(Contact)
admin.site.register(Coordinates)
admin.site.register(Rating)