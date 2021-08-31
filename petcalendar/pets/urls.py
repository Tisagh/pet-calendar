from django.urls import path
from .views import index

app_name = 'pets'

urlpatterns = [
  path('', index, name='index'),
]