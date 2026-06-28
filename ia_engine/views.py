import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from courses.models import Exercicio, LicaoBiblica
from .engine import gerar_dica_exercicio, gerar_explicacao_licao, gerar_devocional

@login_required
@csrf_exempt
def pedir_dica(request, exercicio_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    exercicio = get_object_or_404(Exercicio, id=exercicio_id)
    profile = request.user.profile
    custo = 5

    if profile.pontos_para_ajuda < custo:
        return JsonResponse({
            'error': f'Você precisa de {custo} pontos de ajuda. Complete mais lições para ganhar pontos.',
            'pontos_atual': profile.pontos_para_ajuda,
        }, status=400)

    data = json.loads(request.body) if request.body else {}
    resposta_usuario = data.get('resposta')
    dica = gerar_dica_exercicio(exercicio, resposta_usuario)

    profile.pontos_para_ajuda -= custo
    profile.save()

    return JsonResponse({
        'dica': dica,
        'custo': custo,
        'pontos_restantes': profile.pontos_para_ajuda,
    })

@login_required
@csrf_exempt
def explicar_licao(request, licao_id):
    licao = get_object_or_404(LicaoBiblica, id=licao_id)
    profile = request.user.profile
    custo = 10

    if profile.pontos_para_ajuda < custo:
        return JsonResponse({
            'error': f'Você precisa de {custo} pontos de ajuda.',
            'pontos_atual': profile.pontos_para_ajuda,
        }, status=400)

    explicacao = gerar_explicacao_licao(licao)
    profile.pontos_para_ajuda -= custo
    profile.save()

    return JsonResponse({
        'explicacao': explicacao,
        'custo': custo,
        'pontos_restantes': profile.pontos_para_ajuda,
    })

@login_required
@csrf_exempt
def devocional_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    data = json.loads(request.body)
    tema = data.get('tema', 'fé')
    profile = request.user.profile
    devocional = gerar_devocional(tema, profile.faixa_etaria, profile.nivel_atual)

    return JsonResponse({
        'devocional': devocional,
        'tema': tema,
    })
