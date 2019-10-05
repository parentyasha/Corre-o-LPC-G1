from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, verbose_name='Pessoa',on_delete=models.DO_NOTHING)
    nome = models.CharField(verbose_name='Nome da Pessoa', max_length=50)

    def __str__(self):
        return self.usuario.username

class Funcionario(Pessoa):
    matricula = models.CharField(verbose_name='Matricula do Funcionario', max_length=30)

    def __str__(self):
        return self.matricula

class Departamento(models.Model):
    nome_departamento = models.CharField(verbose_name='Nome do departamento', max_length=30)

    def __str__(self):
        return self.nome_departamento

class Processo(models.Model):
    titulo = models.CharField(verbose_name='Titulo do Processo', max_length=30)
    descricao = models.TextField(verbose_name='Descrição')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    interessada = models.ManyToManyField(Pessoa, related_name='Interessada')
    investigada = models.ManyToManyField(Pessoa, related_name='Investigada')
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo + ' - ' + self.descricao

class Documento(models.Model):
    numero = models.IntegerField(verbose_name='Numero do Documento')
    titulo = models.CharField(verbose_name='Titulo do Processo', max_length=30)
    data = models.DateField(verbose_name='Data')
    processo = models.ForeignKey(Processo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo + ' - ' + self.processo.titulo

class Portaria(Documento):
    nome = models.CharField(verbose_name='nome', max_length=30)

    def __str__(self):
        return self.nome

class Prazo(Documento):
    justificativa = models.CharField(verbose_name='Justificativa', max_length=50)
    prazo_anterior = models.DateField(verbose_name='Data Inicial')
    prazo_seguinte = models.DateField(verbose_name='Data Nova')

    def __str__(self):
        return 'Justificativa do pedido do prazo: ' + self.justificativa + ', data e hora inicial: ' + str(self.prazo_anterior) + ', data e hora nova: ' + str(self.prazo_seguinte)

class Envio(Documento):
    data_envio = models.DateField(verbose_name='Data de envio')
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'data de envio do processo: ' + str(self.data_envio) + ' - ' + 'departamento destino: ' + str(self.departamento_destino)

class Tramitacoes(models.Model):
    data_origem = models.DateField(verbose_name='Data Origem')
    data_destino = models.DateField(verbose_name='Data Destino')
    departamento_origem = models.ForeignKey(Departamento, related_name = 'departamento_origem' ,on_delete=models.DO_NOTHING)
    departamento_destino = models.ForeignKey(Departamento, related_name = 'departamento_destino', on_delete=models.DO_NOTHING)
    processo = models.ForeignKey(Processo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Saiu do departamento: ' + str(self.departamento_origem) + ', para o departamento: ' + str(self.departamento_destino)