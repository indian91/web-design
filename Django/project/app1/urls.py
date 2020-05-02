from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('signup/',views.signup),
    path('login/',views.login),
    path('aftersignup/',views.aftersignup),
    path('afterlogin/',views.login),
]