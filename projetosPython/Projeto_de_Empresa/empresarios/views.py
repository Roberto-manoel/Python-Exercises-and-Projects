from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.views.decorators.csrf import csrf_protect
from datetime import date
from django.utils.safestring import mark_safe
from .models import Empresas

@csrf_protect
@login_required(login_url='/usuarios/login')

def cadastrar_empresa(request):
    if request.method == "GET":
        empresa = Empresas.objects.first()
        tempo_existencia = empresa.tempo_existencia if empresa else None
        return render(request, 'cadastrar_empresa.html', {'tempo_existencia': tempo_existencia})
    
    if request.method == "POST":
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        site = request.POST.get('site')
        tempo_existencia = request.POST.get('tempo_existencia')
        descricao = request.POST.get('descricao')
        data_final = request.POST.get('data_final')
        percentual_equity = request.POST.get('percentual_equity')
        estagio = request.POST.get('estagio')
        area = request.POST.get('area')
        publico_alvo = request.POST.get('publico_alvo')
        valor = request.POST.get('valor')
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')
        
        # Validação básica
        if not nome or not cnpj:
            messages.add_message(request, constants.ERROR, 'Nome e CNPJ são obrigatórios.')
            return redirect('/empresarios/cadastrar_empresa')
        
        try:
            empresa = Empresas(
                user=request.user,
                nome=nome,
                cnpj=cnpj,
                site=site,
                tempo_existencia=tempo_existencia,
                descricao=descricao,
                data_final_captacao=data_final,
                percentual_equity=percentual_equity,
                estagio=estagio,
                area=area,
                publico_alvo=publico_alvo,
                valor=valor,
                pitch=pitch,
                logo=logo
            )
            empresa.save()
            messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {e}')
        
        return redirect('/empresarios/cadastrar_empresa')

@login_required(login_url='/usuarios/login')
def listar_empresas(request):
    if request.method == "GET":
        empresas = Empresas.objects.filter(user=request.user)
        return render(request, 'listar_empresas.html', {'empresas': empresas})

class Empresa:
    @property
    def status(self):
        if date.today() > self.data_final_captacao:
            return mark_safe('<span class="badge bg-success">Captação finalizada</span>')
        return mark_safe('<span class="badge bg-primary">Em captação</span>')

def empresa(request, id):
    empresa = Empresas.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'empresa.html', {'empresa': empresa})
