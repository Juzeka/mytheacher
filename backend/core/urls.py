from django.contrib import admin
from django.urls import path
from teacher.views import CadastrarAulaAPIView, ProfessorAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('professores/', ProfessorAPIView.as_view()),
    path('professores/cadastrar_aula/<int:pk>', CadastrarAulaAPIView.as_view())
]
