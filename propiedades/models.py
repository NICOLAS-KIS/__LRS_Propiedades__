from django.db import models

class Propiedad(models.Model):

    OPERACION_CHOICES = (
        ('V', 'Venta'),
        ('A', 'Alquiler'),
    )
    TIPO_CHOICES = (
        ('C', 'Casa'),
        ('D', 'Departameto'),
        ('T', 'Terreno'),
        ('G', 'Garage'),
        ('P', 'PH'),
        ('O', 'Oficina'),
    )
    ANTIGUEDAD_CHOICES = (
        ('E', 'A Estrenar'),
        ('D', 'Mas de 10 Años'),
        ('V', 'Mas de 20 Años'),
        ('T', 'Mas de 30 Años'),
    )

    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    localidad = models.CharField("Barrio", max_length=50)
    calle = models.CharField(max_length=50)
    piso = models.CharField(max_length=50)
    ambientes = models.IntegerField(default=0)
    superficie_cubierta = models.IntegerField(default=0)
    superficie_descubierta = models.IntegerField(default=0)
    #cochera = models.BooleanField(default=False)

    operacion = models.CharField(max_length=50,choices = OPERACION_CHOICES)
    tipo = models.CharField(max_length=50,choices = TIPO_CHOICES)
    antiguedad = models.CharField(max_length=50,choices = ANTIGUEDAD_CHOICES)

    descripcion = models.CharField(max_length=1000)

    precio = models.IntegerField()
    expensas = models.IntegerField()

    width_modified = models.IntegerField(default=0)
    height_modified = models.IntegerField(default=0)

    image = models.ImageField(null=False, blank=False)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

class PropiedadImagen(models.Model):
    property = models.ForeignKey(Propiedad, related_name='images', on_delete="cascade")
    image = models.ImageField()

    def __str__(self):
        return self.property_id

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

class Photo(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete="cascade", blank=True, null=True )
    image = models.ImageField()
    def __str__(self):
        return u'%s %s' % (self.propiedad, self.image)