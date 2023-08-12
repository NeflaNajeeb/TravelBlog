from django.db import models

# Create your models here.
class tb_Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class tb_teammem(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=150)
    designtn=models.CharField(max_length=250)

    def __str__(self):
        return self.name