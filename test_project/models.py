from django.db import models

# Create your models here.


class Participant(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self): return self.name


class Measurement(models.Model):
    date = models.DateField()
    time = models.TimeField()
    weight = models.DecimalField()
    user = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self): return self.user
