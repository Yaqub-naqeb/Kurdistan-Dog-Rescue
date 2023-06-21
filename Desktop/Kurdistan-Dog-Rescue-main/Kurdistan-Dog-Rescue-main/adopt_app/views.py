from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.
def list_dogs(request):
    dogs = Dog.objects.all()
    context = {'dogs': dogs}
    return render(request, 'adopt_app/adopt.html', context)