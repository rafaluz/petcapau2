from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField('Nome', max_length=70)
    species = models.CharField('Espécie', max_length=70)
    breed = models.CharField('Raça', max_length=70)
    SEX_CHOICES = (('Macho', 'Macho'), ('Femea', 'Femea'),)
    sex = models.CharField('Sexo', max_length=5, choices=SEX_CHOICES, default='Macho')
    birth_date = models.DateField('Data de Nascimento')
    HAIR_CHOICES = (('curto', 'curto'), ('longo', 'longo'), ('encaracolado', 'encaracolado'), ('duplo', 'duplo'))
    hair = models.CharField('Pelagem', max_length=12, choices=HAIR_CHOICES, default='curto')
    tatoo = models.CharField('Identificação ou Tatuagem', max_length=7, blank=True, null=True)
    
    def __str__(self):
        return self.name