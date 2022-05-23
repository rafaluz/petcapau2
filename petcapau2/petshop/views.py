from django.shortcuts import render
from .models import Pet 

# Create your views here.
def HelloWorld(request):
    mensagem = "Olá, mundo!"
    alunos = ['alex', 'jean', 'daniel', 'karielly', 'wanda', 'shara']
    return render(request, 'pet/hello_world.html', {'mensagem':mensagem, 'alunos':alunos})


def ListPet(request):
    pets = Pet.objects.all()
    return render(request, 'pet/pet_list.html',{'pets': pets})

def PetDetail(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pet/pet_detail.html',{'pet': pet})