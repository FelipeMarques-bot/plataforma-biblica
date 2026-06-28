import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SessaoDevocional, MensagemDevocional
from ia_engine.engine import gerar_devocional

@login_required
def chat_view(request):
    sessoes = SessaoDevocional.objects.filter(usuario=request.user).order_by('-data_inicio')[:5]
    sessao_atual = sessoes.first()

    if not sessao_atual:
        sessao_atual = SessaoDevocional.objects.create(
            usuario=request.user,
            tema='fe',
        )
        texto_ia = gerar_devocional('fé', request.user.profile.faixa_etaria, request.user.profile.nivel_atual)
        MensagemDevocional.objects.create(
            sessao=sessao_atual,
            remetente='ia',
            texto=texto_ia,
        )

    mensagens = sessao_atual.mensagens.all()
    mensagens_data = [{'tipo': m.remetente, 'texto': m.texto} for m in mensagens]

    return render(request, 'chat.html', {
        'mensagens_data': json.dumps(mensagens_data),
        'sessao_atual': sessao_atual,
        'sessoes': sessoes,
    })

@login_required
@csrf_exempt
def enviar_mensagem(request, sessao_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    sessao = get_object_or_404(SessaoDevocional, id=sessao_id, usuario=request.user)
    data = json.loads(request.body)
    texto = data.get('texto', '').strip()

    if not texto:
        return JsonResponse({'error': 'Mensagem vazia'}, status=400)

    MensagemDevocional.objects.create(
        sessao=sessao,
        remetente='usuario',
        texto=texto,
    )

    resposta_ia = gerar_devocional(sessao.tema, request.user.profile.faixa_etaria, request.user.profile.nivel_atual)
    MensagemDevocional.objects.create(
        sessao=sessao,
        remetente='ia',
        texto=resposta_ia,
    )

    return JsonResponse({
        'resposta': resposta_ia,
        'data_hora': None,
    })

@login_required
@csrf_exempt
def nova_sessao(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    data = json.loads(request.body)
    tema = data.get('tema', 'fe')

    sessao = SessaoDevocional.objects.create(usuario=request.user, tema=tema)
    texto_ia = gerar_devocional(tema, request.user.profile.faixa_etaria, request.user.profile.nivel_atual)
    MensagemDevocional.objects.create(
        sessao=sessao,
        remetente='ia',
        texto=texto_ia,
    )

    return JsonResponse({
        'sessao_id': sessao.id,
        'mensagem_ia': texto_ia,
    })
