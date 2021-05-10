from django.db import models

class Allcources(models.Model):
    courcename = models.CharField(max_length=200)
    insname = models.CharField(max_length=100)

    def __str__(self):
        return self.courcename

class details(models.Model):
    cource = models.ForeignKey(Allcources, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)