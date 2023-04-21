from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


def homepage(request):
    # return HttpResponse("Jambo Site")
    return render(request=request,
                  template_name="main/home.html",
                  context={"events": Event.objects.all})
