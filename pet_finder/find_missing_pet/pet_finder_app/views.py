from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import Pet

def index(request):
    # Display the list of pets
    pets = Pet.objects.all()
    return render(request, 'index.html', {'pets': pets})
