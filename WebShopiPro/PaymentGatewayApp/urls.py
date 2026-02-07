from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('pay/',views.payment_gateway, name="pay"),
    path('paypage/',views.paypage, name="paypage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.BASE_DIR)