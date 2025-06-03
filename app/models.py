from django.db import models

class Sensores(models.Model):
    SENSOR_CHOICES = [
        ('temperatura', 'temperatura'),
        ('luminosidade', 'luminosidade'),
        ('umidade', 'umidade'),
        ('contador', 'contador'),
    ]
    STATUS_CHOICES = [
        ('ativo', 'ativo'),
        ('inativo', 'inativo'),
    ]

    UNIDADE_CHOICES = [
        ('°C', '°C'),
        ('lux', 'lux'),
        ('%', '%'),
        ('num', 'num'),
    ]
    sensor = models.CharField(max_length=12, choices=SENSOR_CHOICES)
    mac_address = models.CharField(max_length=100)
    unidade_med =  models.CharField(max_length=3, choices=UNIDADE_CHOICES, default= '°C')
    latitude = models.FloatField()
    longitude = models.FloatField()
    status =  models.CharField(max_length=8, choices=STATUS_CHOICES, blank=False)
    
    REQUIRED_FILES = ['sensor', 'mac_address', 'unidade_med', 'latitude', 'longitude', 'status']
    def __str__(self):
        return self.sensor

class Ambientes(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=255, blank=True)
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=255)
    
    
    REQUIRED_FILES = ['ni', 'sig', 'responsavel']

    def __str__(self):
        return str (self.sig)

class Historico(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.sensor
