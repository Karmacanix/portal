from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Expense, ActiveExpenseManager



class ExpenseListView(ListView):
    model = Expense
    context_object_name = "my_favorite_expenses"


class ExpenseDetailView(UpdateView):
    context_object_name = "topexpense"
    queryset = Expense.active_expenses.all()
    success_url = '/expense/list/'
    fields = '__all__'
