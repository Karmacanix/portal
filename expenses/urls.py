from .models import Expense
from .views import ExpenseListView, ExpenseDetailView
from django.urls import path

urlpatterns = [
    path("list/", ExpenseListView.as_view(), name='expense_list'),
    path("<int:pk>/", ExpenseDetailView.as_view(), name='expense_details'),
]