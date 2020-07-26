from django.http import HttpResponse
from django.shortcuts import render

from Plata import models


def index(request):
    try:
        data = models.Data.objects.all()[0].string

    finally:
        return render(request, "index.html",
                  {"data": list(data)})


def send(request, string):
    models.Data.objects.all().delete()
    data = models.Data()
    data.string = string
    data.save()
    return HttpResponse(status=201)
