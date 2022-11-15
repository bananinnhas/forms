from django.shortcuts import render, redirect
from main.forms import CandidatoForm
from main.models import Candidato
# Create your views here.


def get_cadastros(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST) #Armazenando o formulário criado a uma lista
        if form.is_valid():
            print(request.POST)
            alter_form = form.save(commit=False)
            alter_form.mini_cursos = " | ".join(dict(request.POST)['mini_cursos'])

            alter_form.save()

            return redirect("/")
        else:
            form = CandidatoForm

    forms =  CandidatoForm
    candidato = Candidato.objects.all()

    return render(request, "forms.html", {"forms": forms, "candidato": candidato})