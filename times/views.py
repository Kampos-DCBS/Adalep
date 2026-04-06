from django.shortcuts import render, redirect, get_object_or_404
from .models import Time

def lista_times(request):
    times = Time.objects.all()
    return render(request, 'times/lista.html', {'times': times})


def editar_time(request, id):
    time = get_object_or_404(Time, id=id)

    if request.method == 'POST':
        time.nome = request.POST.get('nome')
        time.cidade = request.POST.get('cidade')
        time.fundacao = request.POST.get('fundacao')
        time.save()
        return redirect('lista_times')

    return render(request, 'times/editar.html', {'time': time})


def excluir_time(request, id):
    time = get_object_or_404(Time, id=id)
    time.delete()
    return redirect('lista_times')