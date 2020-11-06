from .models import Badge, Contact, Coordinates, Icon, MenuTypes, Product, ProductImages, Restaurant, RestaurantBadge, RestaurantImages, Review, Tips
from django.shortcuts import render
from rest_framework import viewsets, exceptions, status
from .serializers import (
    MenuTypesSerializer, 
    ProductSerializer, 
    RestaurantSerializer,
    BadgeSerializer,
    CoordinatesSerializer,
    IconSerializer,
    ContactSerializer,
    UserBadgeSerializer,
    RestaurantImagesSerializer,
    ProductImagesSerializer,
    IconSerializer,
    TipsSerializer,
    BadgeSerializer,
    RestaurantBadgeSerializer,
    ReviewSerializer
)



class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    authentication_classes = []
    permission_classes = []


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = []
    permission_classes = []
	

class MenuTypesViewSet(viewsets.ModelViewSet):
    serializer_class = MenuTypesSerializer
    queryset = MenuTypes.objects.all()
    authentication_classes = []
    permission_classes = []


class BadgeViewSet(viewsets.ModelViewSet):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    authentication_classes = []
    permission_classes = []


class IconViewSet(viewsets.ModelViewSet):
    serializer_class = IconSerializer
    queryset = Icon.objects.all()
    authentication_classes = []
    permission_classes = []


class CoordintaesViewSet(viewsets.ModelViewSet):
    serializer_class = CoordinatesSerializer
    queryset = Coordinates.objects.all()
    authentication_classes = []
    permission_classes = []


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    authentication_classes = []
    permission_classes = []


class UserBadgeViewSet(viewsets.ModelViewSet):
    serializer_class = UserBadgeSerializer
    queryset = Badge.objects.all()
    authentication_classes = []
    permission_classes = []


class RestaurantImagesViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantImagesSerializer
    queryset = RestaurantImages.objects.all()
    authentication_classes = []
    permission_classes = []


class ProductImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImagesSerializer
    queryset = ProductImages.objects.all()
    authentication_classes = []
    permission_classes = []


class TipsViewSet(viewsets.ModelViewSet):
    serializer_class = TipsSerializer
    queryset = Tips.objects.all()
    authentication_classes = []
    permission_classes = []


class RestaurantBadgeViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantBadgeSerializer
    queryset = RestaurantBadge.objects.all()
    authentication_classes = []
    permission_classes = []


class ReviewBadgeViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    authentication_classes = []
    permission_classes = []
