from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serilaizer import ExpenseListSerializer
from .models import Expense
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.


class ExpenseListAPIView(ListCreateAPIView):

    serializer_class = ExpenseListSerializer
    queryset = Expense.objects.all()

    permissions = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseListSerializer
    queryset = Expense.objects.all()

    permissions = (permissions.IsAuthenticated,IsOwner)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
