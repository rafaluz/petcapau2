from django.urls import path
from . import views

app_name = "petshop"

urlpatterns = [
    path('olamundo', views.HelloWorld),
    path('pet/list', views.ListPet.as_view(), name='pet_list'),
    path('pet/details/<int:pk>', views.PetDetail.as_view(), name='pet_detail'),
    path('pet/create', views.PetCreate.as_view(), name='pet_create'),
    path('pet/update/<int:pk>', views.PetUpdate.as_view(), name='pet_update'),
    path('pet/delete/<int:pk>', views.PetDelete.as_view(), name='pet_delete'),
]