from django.contrib import admin
from .models import (
  Restaurant, 
  RestaurantImages,
  Contact,
  Coordinates,
  Rating,
  Icon,
  Review,
  Tips,
  Badge,
  RestaurantBadge,
  UserBadge,
  UserRestaurants,
  MenuTypes,
  Product,
  ProductImages
  # Menu
)


admin.site.register(Restaurant)
admin.site.register(RestaurantImages)
admin.site.register(Contact)
admin.site.register(Coordinates)
admin.site.register(Rating)
admin.site.register(Icon)
admin.site.register(Review)
admin.site.register(Tips)
admin.site.register(Badge)
admin.site.register(RestaurantBadge)
admin.site.register(UserBadge)
admin.site.register(UserRestaurants)
admin.site.register(MenuTypes)
admin.site.register(Product)
admin.site.register(ProductImages)
# admin.site.register(Menu)