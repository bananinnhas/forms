from django.shortcuts import render, redirect
from main.forms import CandidatoForm
from main.models import Candidato
# Create your views here.


def get_cadastros(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = CandidatoForm()
    else:
        form = CandidatoForm()

    return render(request,'forms.html', { 'form' : form})