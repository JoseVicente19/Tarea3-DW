# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Publicaciones(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateField(blank=True, null=True)
    autor = models.CharField(max_length=255, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo}"

    class Meta:
        managed = False
        db_table = 'publicaciones'
