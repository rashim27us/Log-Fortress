from django.db import models

class NetworkLogs(models.Model):
    datetime = models.DateTimeField()
    bytes_recieved= models.BigIntegerField(null=True, blank=True)
    bytes_sent = models.BigIntegerField(null=True, blank=True)

