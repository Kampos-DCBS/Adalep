from django.shortcuts import render
from .models import Time

def lista_times(request):
    times = Time.objects.all()
    return render(request, 'times/lista.html', {'times': times})