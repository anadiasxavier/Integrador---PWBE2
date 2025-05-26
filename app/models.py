from django.db import models

class Sensores(models.Model):
    SENSOR_CHOICES = [
        ('T', 'Temperatura'),
        ('L', 'Luminosidade'),
        ('U', 'Umidade'),
        ('C', 'Contador'),
    ]
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]

    UNIDADE_CHOICES = [
        ('°C', '°C'),
        ('lux', 'lux'),
        ('%', '%'),
        ('num', 'num'),
    ]
    sensor = models.CharField(max_length=1, choices=SENSOR_CHOICES)
    mac_address = models.CharField(max_length=100)
    unidade_med =  models.CharField(max_length=3, choices=UNIDADE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status =  models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.sensor

class Ambientes(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=255)
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=255)

    def __str__(self):
        return str (self.sig)

class Historico(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self):
        return self.sensor
