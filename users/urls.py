from . import views
from django.urls import path
from users.views import index

urlpatterns = [
    path('', views.index, name='index')
]
