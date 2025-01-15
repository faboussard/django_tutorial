from django.contrib import admin
from .models import Question, Choice

# Permet d'ajouter des choix directement dans la page de la question
class ChoiceInline(admin.TabularInline):  # ou admin.StackedInline
    model = Choice
    extra = 3  # Nombre de choix vides proposés par défaut

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    inlines = [ChoiceInline]  # Ajoute les choix dans la page Question

# Enregistre Question avec la configuration personnalisée
admin.site.register(Question, QuestionAdmin)
