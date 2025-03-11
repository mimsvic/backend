from django.shortcuts import render
from .models import Cadastro, Disciplina
from .serializer import CadastroSerializer, DisciplinaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Função para listar e criar professores
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_professores(request):
    if request.method == 'GET':
        queryset = Cadastro.objects.all()
        serializer = CadastroSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Função para buscar professores por nome
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buscar_nome_professor(request):
    termo = request.query_params.get('nome', '') 
    if termo:
        professores = Cadastro.objects.filter(nome__icontains=termo) 
    else:
        professores = Cadastro.objects.all()
    
    serializer = CadastroSerializer(professores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessoresView(ListCreateAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = [IsAuthenticated]


class ProfessoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = [IsAuthenticated]


class ProfessoresSearchView(ListAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['nome']


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_disciplinas(request):
    if request.method == 'GET':
        queryset = Disciplina.objects.all()
        serializer = DisciplinaSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buscar_nome_disciplina(request):
    termo = request.query_params.get('nome', '')  # Método correto de pegar o parâmetro
    if termo:
        disciplinas = Disciplina.objects.filter(nome__icontains=termo)  # Filtro correto
    else:
        disciplinas = Disciplina.objects.all()
    
    serializer = DisciplinaSerializer(disciplinas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class DisciplinasView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]


class DisciplinasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    # permission_classes = [IsAuthenticated]


class DisciplinasSearchView(ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

