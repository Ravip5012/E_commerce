from django.urls import path
from .import views

urlpatterns=[
    path("register/",views.webshopi_registerpage, name="register"),
    path("login/",views.UserCustomLogin.as_view(), name="login"),
    path("logout/",views.logoutview,name="logout"),
    path("profile/",views.profile_view, name='profile'),
    path("changepass/",views.change_password, name='changepass')
]