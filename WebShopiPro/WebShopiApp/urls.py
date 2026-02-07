from django.urls import path
from .import views


urlpatterns = [
     path('', views.index, name="index"),
    # path('load/',views.load_products, name='load'),
    # path('product/<int:product_id/', views.product, name='product'),
    path("product/<int:pk>/", views.product, name="product"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add-to-cart"),
    path("cart/update/<int:item_id>/", views.update_cart_item, name="update-cart-item"),
    path("cart/remove/<int:item_id>/", views.remove_cart_item, name="remove-cart-item"),
    path("search-products/", views.search_products, name="search-products"),
    path("search/", views.search, name="search"),
    path("contact",views.contact_page,name="contact")
    # path('checkout/',views.checkout, name="checkout"),
    # path('payment-success/', views.payment_success, name='payment-success'),
]
   
