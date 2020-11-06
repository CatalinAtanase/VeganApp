from django.urls import include, path
from rest_framework import routers
from .views import (
    MenuTypesViewSet, 
    RestaurantViewSet, 
    ProductViewSet,
    BadgeViewSet,
    IconViewSet,
    CoordintaesViewSet,
    ContactViewSet,
    UserBadgeViewSet,
    RestaurantImagesViewSet,
    ProductImagesViewSet,
    TipsViewSet,
    RestaurantBadgeViewSet,
    ReviewBadgeViewSet,
)

router = routers.DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('products', ProductViewSet)
router.register('menu-types', MenuTypesViewSet)
router.register('badges', BadgeViewSet)
router.register('icons', IconViewSet)
router.register('coordinates', CoordintaesViewSet)
router.register('contacts', ContactViewSet)
router.register('user-badges', UserBadgeViewSet)
router.register('restaurant-images', RestaurantImagesViewSet)
router.register('product-images', ProductImagesViewSet)
router.register('tips', TipsViewSet)
router.register('restaurant-badges', RestaurantBadgeViewSet)
router.register('reviews', ReviewBadgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
