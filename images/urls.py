from django.urls import path
from .views import home, food_view, food_details_view

urlpatterns = [
    path('', home, name='home'),
    path('images/', food_view, name='image_list'), 
    path('images/<int:pk>/', food_details_view, name='food_details'), 
]