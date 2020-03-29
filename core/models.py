from django.db import models

# Create your models here.
class Links(models.Model):
    name = models.URLField(max_length=254)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.name 


#---------REGION PAGE---------
class Regions(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=254)
    infected = models.IntegerField(verbose_name="Cant. Infectados")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ('infected',)

    def __str__(self):
        return self.name 

#---------CHILE PAGE----------
class Chile(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=254)
    prom_factor = models.CharField(verbose_name="Factor promedio", max_length=254)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.name

class ChileData(models.Model):
    name = models.IntegerField(verbose_name="Datos de Chile")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class World(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=254)
    prom_factor = models.CharField(verbose_name="Factor promedio", max_length=254)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        ordering = ('-prom_factor',)

    def __str__(self):
        return self.name

class Page(models.Model):
    infected = models.CharField(verbose_name="Infectados", max_length=254)
    recovered = models.CharField(verbose_name="Recuperados", max_length=254)
    dead = models.CharField(verbose_name="Muertos", max_length=254)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.infected