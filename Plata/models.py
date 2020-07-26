from django.db import models


class Data(models.Model):
    string = models.CharField(max_length=6)