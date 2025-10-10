from django.db import models

class estudiantes(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    curso = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"

class Meta:
        db_table = 'estudiantes' 

