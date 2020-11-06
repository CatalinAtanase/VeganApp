from rest_framework import serializers
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


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = (
            "latitude",
            "longitude",
        )
        # depth = 2


class ContactSerializer(serializers.ModelSerializer):
    coordinates = CoordinatesSerializer(many=True)

    class Meta:
        model = Contact
        fields = (
            "phone_number",
            "email",
            "address",
            "website_url",
            "coordinates",
        )
        # depth = 1


class MenuTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTypes
        fields = "__all__"
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    type = MenuTypesSerializer()

    class Meta:
        model = Product
        fields = (
            "name",
            "price",
            "ingredients",
            "type",
        )
        # depth = 1


class RestaurantImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImages
        fields = (
            "image",
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        depth = 1


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = (
            "icon",
            "name",
            "description",
        )
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 1


class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = "__all__"
        depth = 1


class BadgeSerializer(serializers.ModelSerializer):
    icon = IconSerializer()

    class Meta:
        model = Badge
        fields = (
            "color",
            "icon",
        )


class RestaurantBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer()

    class Meta:
        model = RestaurantBadge
        fields = (
            "badge",
            "added_at"
        )


class UserBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBadge
        fields = "__all__"
        depth = 1


class UserRestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRestaurants
        fields = "__all__"
        depth = 1


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"
        depth = 1


class RestaurantSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=True)
    restaurant_badges = RestaurantBadgeSerializer(many=True)
    restaurant_products = ProductSerializer(many=True)
    images = RestaurantImagesSerializer(many=True)
    # tips maybe??

    class Meta:
        model = Restaurant
        # fields = "__all__"
        fields = (
            "name", 
            "description", 
            "contact", 
            "images", 
            'restaurant_badges',
            'restaurant_products',
            "created_at", 
            "updated_at",
        )


class RestaurantMapSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=True)
    restaurant_badges = RestaurantBadgeSerializer(many=True)
    restaurant_tips = TipsSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = (
            "name", 
            "description", 
            "contact", 
            "images", 
            'restaurant_badges',
            'restaurant_tips',
            "created_at", 
            "updated_at",
        )