from .models import UserActivityLog

def log_activity(usuario, tipo_atividade, descricao='', referencia='', xp_ganho=0):
    UserActivityLog.objects.create(
        usuario=usuario,
        tipo_atividade=tipo_atividade,
        descricao_resumida=descricao,
        referencia=referencia,
        xp_ganho=xp_ganho,
    )
