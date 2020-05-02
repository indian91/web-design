from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
]