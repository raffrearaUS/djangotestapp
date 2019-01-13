from django.db import models


class Diario(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    username = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Noticia(models.Model):
    usuarios = models.ManyToManyField(Usuario)
    fecha = models.DateTimeField()
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE)
    titular = models.CharField(max_length=50)
    autores = models.ManyToManyField('Autor')
    resumen = models.TextField()
    tipos = [('Deportes', 'Deportes'), ('Cultura', 'Cultura'), ('Politica', 'Politica'), ('Economia', 'Economia'),
             ('Actualidad', 'Actualidad')]
    tipo = models.CharField(max_length=100, choices=tipos)

    def __str__(self):
        return self.titular


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre
