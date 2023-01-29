from django.db import models

class UploadFile(models.Model):
    file = models.FileField(upload_to="")


class ContentFile(models.Model):
    type = models.CharField( max_length= 1 )
    date = models.CharField( max_length= 8)
    value = models.IntegerField()
    cpf = models.CharField( max_length= 11)
    card = models.CharField( max_length= 12)
    hour = models.CharField( max_length= 6)
    owner = models.CharField( max_length= 14)
    name = models.CharField( max_length= 19)