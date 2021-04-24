from django.db import models


class NintendoModel(models.Model):
    character_name = models.CharField(max_length=50)
    character_level = models.IntegerField()
    character_description = models.TextField(max_length=200, blank=True, null=True)
    character_year = models.DateField(auto_now=False, auto_now_add=False)
    character_game = models.CharField(max_length=50)
