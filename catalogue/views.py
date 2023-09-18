from typing import Any
from django import forms 
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from catalogue.models import Catalog, Service

# Create your views here.
def show_catalog(request):
    return render(request, "catalogue/catalog.html", {'catalog': Catalog.objects.all()})


def show_nav_sidebar(request):
    return render(request, "catalogue/catalog_services.html", {"catalog": Catalog.objects.all()})


class CatalogCreateView(CreateView):
    model = Catalog
    fields = '__all__'
    template_name = "catalogue/catalog_form.html"
    success_url = '/catalog/list/'
    

class CatalogUpdateView(UpdateView):
    model = Catalog
    success_url = '/catalog/list/'
    fields = '__all__'
    template_name = "catalogue/catalog_form.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        services = Service.objects.filter(category_id = self.object.id)
        context = super().get_context_data(**kwargs)
        print(services)
        context["service_list"] = services
        return context


class SidebarListView(ListView):
    model = Catalog
    template_name = "catalogue/catalog_services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rns = Catalog.objects.root_nodes()
        print(rns)
        context["top_level_nodes"] = rns
        return context


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'category', 'cost']
    template_name = "catalogue/service_form.html"
    success_url = '/catalog/list/'
    
    def get_initial(self) -> dict[str, Any]:
        initial = super(ServiceCreateView, self).get_initial()
        initial = initial.copy()
        initial['category'] = Catalog.objects.get(id = self.kwargs.get("catalog_id"))
        return initial
        
    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        form.fields['category'].widget = forms.HiddenInput()
        return form


class ServiceListView(ListView):
    model = Service
    template_name = "catalogue/catalog_services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_obj = Catalog.objects.get(id=self.kwargs.get("catalog_id"))
        services = Service.objects.filter(category=cat_obj)
        cat_tree = Catalog.objects.all()
        context["services"] = services
        context["services_for_catalog_item"] = cat_obj
        context["catalog_list"] = cat_tree
        print("all catalogue items:", cat_tree, "catalog item:", cat_obj, "services for catalog item:", services)
        return context   