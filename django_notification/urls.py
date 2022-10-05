
from django.contrib import admin
from django.urls import path, include
from notification.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
