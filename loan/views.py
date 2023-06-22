from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from loan.serializers import LoanSerializer
from .models import Loan

class LoanView(APIView):
    # Dei um jeitinho de fazer um POST tanto para consultar a proposta quanto para criar sei que não é a melhor prática porém foi mais fácil fazer assim
    def post(self, request):
        try:
            name = request.data['name']
            cpf = request.data['cpf']
            
            loan = Loan(name=name, cpf=cpf)
            loan.save()
            return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            name = request.data['name']
            cpf = request.data['cpf']

            try:
                loan = Loan.objects.get(name=name, cpf=cpf)
                return Response(LoanSerializer(loan).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(f'Error creating loan request {str(e)}', status=status.HTTP_400_BAD_REQUEST)
