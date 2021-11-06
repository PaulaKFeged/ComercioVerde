from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here. aquí va el crud


class Alimentos(models.Model):
    NombreAlimento=models.CharField(max_length=100, null=True, blank=True)
    PrecioAlimento=models.FloatField(max_length=7,null=True,blank=True)
    UnidadAlimento=models.CharField(max_length=100, null=True, blank=True)
    CantidadAlimento=models.FloatField(max_length=100, null=True, blank=True)
    Fotoalimento=models.ImageField(upload_to='alimento',null=True,blank=True)
    FechaelaboracionAl=models.DateField(null=True,blank=True)
    FechavencimientoAl=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.NombreAlimento

    @property
    def numal(self):
        num = self.NombreAlimento.all()
        return len(num)


class Productos_Organicos(models.Model):
    NombreProducto=models.CharField(max_length=100, null=True, blank=True)
    PrecioProducto=models.FloatField(max_length=7,null=True,blank=True)
    DescripcionProducto=models.CharField(max_length=500, null=True, blank=True)
    FotoProducto=models.ImageField(upload_to='producto',null=True,blank=True)
    FechaelaboracionPR=models.DateField(null=True,blank=True)
    FechavencimientoPR=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.NombreProducto

class Artesanias(models.Model):
    NombreArtesania=models.CharField(max_length=100,null=True,blank=True)
    PrecioArtesania=models.FloatField(max_length=7,null=True,blank=True)
    DescripcionArtesania=models.CharField(max_length=500, null=True, blank=True)
    FotoArtesania=models.ImageField(upload_to='artesania',null=True,blank=True)

    def __str__(self):
        return self.NombreArtesania


class Carritocompras(models.Model):
    usuario=models.CharField(max_length=100,null=True,blank=True)
    fecha=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.usuario

    def total(self):

        pass

class Items(models.Model):
    artesanias=models.ManyToManyField(Artesanias)
    alimentos=models.ManyToManyField(Alimentos)
    productos=models.ManyToManyField(Productos_Organicos)

    carrito=models.ForeignKey(Carritocompras,on_delete=models.CASCADE)

    def suma(Items):
        pass
    

