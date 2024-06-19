from django.db import models
import jsonfield
class data(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)  # Asegura que la clave es un campo de texto

    def __str__(self):
        # Retorna una representación en cadena del objeto, combinando nombre y clave
        return f"{self.nombre} - {self.clave}"
    
class SensorData(models.Model):
    Id = models.AutoField(primary_key=True)
    Cliente = models.CharField(max_length=100)
    Fecha_carga = models.DateTimeField()
    DB_information = models.JSONField()

    class Meta:
        db_table = 'data_sensor'



class ControlData(models.Model):
    cliente = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    control_data =  models.CharField(max_length=255)

    class Meta:
        db_table = 'control_data'


class Support(models.Model):
    cliente = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    support_information = models.CharField(max_length=255)
    class Meta:
        db_table = 'support'
