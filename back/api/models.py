from django.db import models

class Cadastro(models.Model):
    ni = models.CharField(max_length=15)  # Número de identificação do aluno
    nome = models.CharField(max_length=255)  # Nome do aluno
    email = models.EmailField()  # Email do aluno
    cel = models.CharField(max_length=255)  # Celular do aluno
    ocup = models.FloatField()  # Ocupação, pode ser a carga horária de trabalho ou outro dado relevante

    def __str__(self):
        return self.nome



class Disciplina(models.Model):
    nome = models.CharField(max_length=100)  # Nome da disciplina
    sigla = models.CharField(max_length=20)  # Sigla da disciplina
    curso = models.CharField(max_length=50, default='desenvolvimento de sistemas')  # Curso da disciplina
    semestre = models.CharField(max_length=20, default='2º Semestre')  # Semestre de oferta da disciplina
    carga_horaria = models.IntegerField(default=0)  # Carga horária da disciplina

    def __str__(self):
        return self.nome



class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)  # Disciplina associada à turma
    codigo_turma = models.CharField(max_length=50)  # Código identificador da turma (ex: "D1", "M1")
    professor = models.CharField(max_length=255)  # Nome do professor
    ano = models.IntegerField()  # Ano da turma
    semestre = models.CharField(max_length=20, default='2º Semestre')  # Semestre do ano

    def __str__(self):
        return f"{self.disciplina.nome} - {self.codigo_turma}"



class Matricula(models.Model):
    aluno = models.ForeignKey(Cadastro, on_delete=models.CASCADE)  # Aluno matriculado
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)  # Turma onde o aluno está matriculado
    data_matricula = models.DateField(auto_now_add=True)  # Data de matrícula

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma.codigo_turma}"

