from django.db import models

# Modelo Cadastro
class Cadastro(models.Model):
    ni = models.CharField(max_length=15)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cel = models.CharField(max_length=255)
    ocup = models.FloatField()

    def __str__(self):
        return self.nome


# Modelo Disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    curso = models.CharField(max_length=50, default='desenvolvimento de sistemas')  # Default para curso
    semestre = models.CharField(max_length=20, default='2º Semestre')  # Default para semestre
    carga_horaria = models.IntegerField(default=0)  # Default para carga horária, caso não especificado

    def __str__(self):
        return self.nome
