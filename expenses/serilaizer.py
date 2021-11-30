from rest_framework import serializers
from .models import Expense


class ExpenseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['date', 'description', 'amount', 'category']
