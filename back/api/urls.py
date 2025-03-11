from django.urls import path
from .views import (
    listar_professores, ProfessoresView, ProfessoresDetailView, buscar_nome_professor, ProfessoresSearchView, DisciplinasView, DisciplinasDetailView 
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Endpoints de Professores
    path('professores', listar_professores),
    path('prof', ProfessoresView.as_view()),
    path('id/<int:pk>', ProfessoresDetailView.as_view()),
    path('buscar/nome/', buscar_nome_professor),
    path('search/', ProfessoresSearchView.as_view()),

    # Endpoints de JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints de Disciplinas
    path('disciplinas/', DisciplinasView.as_view()),  # Lista todas as disciplinas
    path('disciplinas/<int:pk>', DisciplinasDetailView.as_view()),  # Busca uma disciplina específica
]
