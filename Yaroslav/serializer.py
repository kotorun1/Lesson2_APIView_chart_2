from rest_framework import serializers
from .models import Product
from .models import Basket


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    cost = serializers.IntegerField(min_value=0)
    description = serializers.IntegerField()
    basket_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.description = validated_data.get('description', instance.description)
        instance.basket_id = validated_data.get('basket_id', instance.basket_id)
        instance.save()
        return instance
    
class BasketSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    products_id = serializers.IntegerField()

    def create(self, validated_data):
        return Basket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.products_id = validated_data.get('products_id', instance.products_id)
        instance.save()
        return instance