from django.shortcuts import render, redirect
from django.core.mail import send_mail
from decouple import config
from .models import SolicitacaoServico
from .forms import SolicitacaoServicoForm

def solicitar_servico(request):
    if request.method == 'POST':
        form = SolicitacaoServicoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save()

            # Enviar e-mail de confirmação
            send_mail(
                'Confirmação de Solicitação de Serviço',
                f'Olá {solicitacao.nome_completo},\n\n'
                f'Sua solicitação para o serviço {solicitacao.servico} foi recebida com sucesso.\n\n'
                f'Para mais informações, por favor, visite nosso site: https://rb-tecnologia-482d1af01ada.herokuapp.com/\n\n'
                f'Você também pode nos seguir nas redes sociais:\n'
                f'Facebook: https://www.facebook.com/profile.php?id=100072623021022&mibextid=ZbWKwL\n\n'
                f'Instagram: https://www.instagram.com/invites/contact/?i=1ugu7iacbaw97&utm_content=mng9rof\n\n'
                f'YouTube: https://youtube.com/@rbtecnologia774?si=kEBQ9539oF6Kaphf\n\n'
                f'Se você tiver alguma dúvida, por favor, envie um e-mail para roberto.programadortech@gmail.com\n\n'
                f'Atenciosamente,\n'
                f'Equipe da RB Tecnologia',
                config('EMAIL_HOST_USER'),
                [solicitacao.email],
                fail_silently=False,
            )

            return redirect('index')
    else:
        form = SolicitacaoServicoForm()

    return render(request, 'service/solicitar_servico.html', {'form': form})

def index(request):
    return render(request, 'service/index.html', {})
