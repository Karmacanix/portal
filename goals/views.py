from django.shortcuts import render
from django.forms import ModelForm, BaseModelFormSet, modelform_factory, Textarea
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Goal, ActiveGoalManager


class GoalListView(ListView):
    model = Goal
    context_object_name = "my_favorite_goals"


class GoalDetailView(UpdateView):
    context_object_name = "topgoal"
    queryset = Goal.active_goals.all()
    success_url = '/goal/list/'
    fields = '__all__'