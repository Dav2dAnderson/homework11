from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Expenses
from .serializers import ExpensesSerializer
# Create your views here.


class ExpensesViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

    def get_permissions(self):
        if self.request.method in ["POST", "DELETE", "PUT"]:
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    