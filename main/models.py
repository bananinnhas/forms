from django.db import models

# Create your models here.
LISTA_CURSO= [
    ('Curso técnico', 'Curso técnico'),
    ('ADS', 'ADS'),
]

LISTA_GENERO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Candidato(models.Model):
    nome_candidato = models.CharField(verbose_name="Nome:", max_length=100)
    cpf_candidato = models.CharField(verbose_name="CPF:", max_length=11)
    nasc_candidato = models.DateField(verbose_name="Nascimento: ")
    email_candidato = models.EmailField( verbose_name="Email: ")
    endereco_candidato = models.CharField(max_length=255, verbose_name="Endereço:" )
    genero_candidato = models.CharField(choices=LISTA_GENERO,verbose_name="Sexo: ", max_length=50, blank=True)
    curso_candidato = models.CharField(choices=LISTA_CURSO, max_length=50, verbose_name="Curso:")
    minicursos = models.ManyToManyField(MiniCurso)

    def __str__(self) -> str:
        return self.nome
   
    
    
 
 