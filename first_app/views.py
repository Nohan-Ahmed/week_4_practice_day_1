from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    return render(request, './first_app/home.html',
                  {'form': forms.ExampleForm()})
