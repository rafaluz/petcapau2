from django.urls import path
from . import views

app_name = "petshop"

urlpatterns = [
    path('olamundo', views.HelloWorld),
    path('pet/list', views.ListPet, name='list_pet'),
    path('pet/details/<int:pk>', views.PetDetail, name='pet_detail'),
]