from django.db import models
from django.contrib.auth.models import User





class ProductsOfWebShopi(models.Model):
    title = models.CharField(max_length=100, default="Unknown")
    price = models.FloatField(default=0.00)
    brand = models.CharField(max_length=50, default="Unknown")
    category = models.CharField(max_length=50, default="Unknown")
    rating = models.FloatField(default=0.0)
    reviews = models.CharField(max_length=200)
    description = models.TextField(default="Unknown")
    thumbnail = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        return self.title



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(ProductsOfWebShopi, on_delete=models.CASCADE)   
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
    


