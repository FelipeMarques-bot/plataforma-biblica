from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'faixa_etaria', 'nivel_atual', 'xp_total', 'streak_atual', 'nivel']
    search_fields = ['usuario__username', 'usuario__email']
