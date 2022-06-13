from django.shortcuts import render
from .models import Pet 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
def HelloWorld(request):
    mensagem = "Olá, mundo!"
    alunos = ['alex', 'jean', 'daniel', 'karielly', 'wanda', 'shara']
    return render(request, 'pet/hello_world.html', {'mensagem':mensagem, 'alunos':alunos})

class ListPet(ListView):
    model = Pet
    template_name = 'pet/pet_list.html'

class PetDetail(DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html' 

class PetCreate(CreateView):
    model = Pet
    template_name = 'pet/pet_create.html'
    # fields = ['name','species','breed','sex','birth_date','hair','tatoo']
    fields = '__all__'
    # success_url = reverse_lazy('petshop:pet_list')

    def get_success_url(self):
        return reverse('petshop:pet_list')


class PetUpdate(UpdateView):
    model = Pet
    template_name = 'pet/pet_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('petshop:pet_list')

class PetDelete(DeleteView):
    model = Pet
    template_name = 'pet/pet_confirm_delete.html'
    success_url = reverse_lazy('petshop:pet_list')