from rest_framework import serializers
from core.models import Product, Review


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
