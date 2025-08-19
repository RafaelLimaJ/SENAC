from django.db import models

class CarrosselSlide(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='carousel/')
    legenda = models.CharField(max_length=300, blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='products/')
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class SecaoSobre(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.titulo
