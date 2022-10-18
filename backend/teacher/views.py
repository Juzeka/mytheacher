from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from teacher.serializers import (
    AulasSerializer, Aula,
    CadastrarAulaSerializer,
    ProfessorSerializer, Professor
)

class ProfessorAPIView(APIView):
    def get(self, request, format=None):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)

        return Response(serializer.data, status=HTTP_200_OK)


class CadastrarAulaAPIView(APIView):
    def post(self, request, pk, format=None):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = CadastrarAulaSerializer(data=request.data)

        if serializer.is_valid():
            aula = Aula(
                professor=professor,
                nome=serializer.validated_data.get('nome'),
                email=serializer.validated_data.get('email')
            )
            aula.save()
            aula_serializer = AulasSerializer(aula, many=False)

            return Response(aula_serializer.data, status=HTTP_201_CREATED)

        return Response(
            {
                'message': 'Erro de validação',
                'erros': serializer.errors
            },
            status=HTTP_400_BAD_REQUEST
        )