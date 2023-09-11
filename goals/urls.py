
from .models import Goal
from .views import GoalListView, GoalDetailView
from django.urls import path

urlpatterns = [
    path("list/", GoalListView.as_view(), name='goal_list'),
    path("<int:pk>/", GoalDetailView.as_view(), name='goal_details'),
]