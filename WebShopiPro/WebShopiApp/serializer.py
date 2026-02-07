# from rest_framework import serializers
# from .import models


# class CartSerializer(serializers.ModelSerializer):
#     product_title = serializers.CharField(source="product.title", read_only=True)
#     product_price = serializers.FloatField(source="product.price", read_only=True)
#     image_url = serializers.CharField(source="product.image_url", read_only=True)
#     total_price = serializers.SerializerMethodField()

#     class Meta:
#         model = models.CartItem
#         fields = ["id", "product_title", "product_price", "image_url", "quantity", "total_price"]

#     def get_total_price(self, obj):
#         return obj.total_price()
