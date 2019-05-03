from django.db import models
from django.core.validators import MaxValueValidator

class Usuario(models.Model):

    idUsuario = models.IntegerField("idsite",primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=80)
    nascimento = models.DateField("Nascimento")
    CPF = models.IntegerField("CPF", unique=True, validators=[MaxValueValidator(99999999999)])

    def _str_ (self):
        return self.nome


class Aluno(models.Model):

    RA = models.IntegerField("Matricula",primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=80)
    nascimento = models.DateField("Nascimento")
    CPF = models.IntegerField("CPF", unique=True, validators=[MaxValueValidator(99999999999)])
    endereco = models.CharField("Endereco",max_length=120)
    complemento = models.CharField("Complemento",max_length=20,null=True,blank=True)
    telefone = models.IntegerField("Telefone", validators=[MaxValueValidator(99999999999)])
    curso = models.ForeignKey("Curso", on_delete = models.CASCADE, default="", editable=False)

    def _str_ (self):
        return self.nome

class Professor(models.Model):

    idProf = models.IntegerField("Identificacao",primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=80)
    nascimento = models.DateField("Nascimento")
    CPF = models.IntegerField("CPF", unique=True, validators=[MaxValueValidator(99999999999)])
    endereco = models.CharField("Endereco",max_length=120)
    complemento = models.CharField("Complemento",max_length=20,null=True,blank=True)
    telefone = models.IntegerField("Telefone", validators=[MaxValueValidator(99999999999)])

    def _str_ (self):
        return self.nome

class Curso(models.Model):

    idCurso = models.IntegerField("Curso",primary_key=True)
    nomeCurso = models.CharField("Nome",max_length=30)
    descricao = models.CharField("Descricao",max_length=100)
    sigla = models.CharField("Sigla", max_length=2)
    duracao = models.CharField("Duracao do Curso", max_length=20)
    coordenador = models.ForeignKey("Coordenador", on_delete = models.CASCADE, default="", editable=False)

    def _str_ (self):
        return self.nomeCurso


class Disciplina(models.Model):

    idDisciplina = models.IntegerField("Disciplina",primary_key=True)
    nomeDisc = models.CharField("Nome da disciplina", max_length=50)
    descricao = models.CharField("Descricao", max_length=100)
    horario = models.DateTimeField(auto_now=False, auto_now_add=False)
    cargaHoraria = models.CharField("Carga", max_length=20)
    curso = models.ForeignKey("Curso", on_delete = models.CASCADE, default="", editable=False)
    professor = models.ForeignKey("Professor", on_delete = models.CASCADE, default="", editable=False)

    def _str_ (self):
        return self.nomeCurso

class Coordenador(models.Model):

    idCoord = models.IntegerField("Coordenador",primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=80)
    nascimento = models.DateField("Nascimento")
    CPF = models.IntegerField("CPF", unique=True, validators=[MaxValueValidator(99999999999)])
    endereco = models.CharField("Endereco",max_length=120)
    complemento = models.CharField("Complemento",max_length=20,null=True,blank=True)
    telefone = models.IntegerField("Telefone", validators=[MaxValueValidator(99999999999)])

    def _str_ (self):
        return self.nomeCurso
    


    












    
