from django.shortcuts import render
from .models import Kitchen

# Create your views here.
def home(request):
    return render(request, 'seller/sellerhome.html')

def dashboard(request):
    kitchens = Kitchen.objects.all()  # Fetch all kitchen products
    return render(request, 'seller/sellerhome.html', {'kitchens': kitchens})