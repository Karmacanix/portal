from typing import Any
from django import forms
from django.db import models 
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from catalogue.models import Catalog, Service
from home.views import get_complete_name
from cart.views import ShoppingCart


# Create your views here.
def show_catalog(request):
    return render(request, "catalogue/catalog.html", {'catalog': Catalog.objects.all()})


def show_nav_sidebar(request):
    return render(request, "catalogue/catalog_services.html", {"catalog": Catalog.objects.all()})


class CatalogCreateView(CreateView):
    model = Catalog
    fields = ('name', 'parent')
    template_name = "catalogue/catalog_new_form.html"
    success_url = '/catalog/list/'
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['parent'].widget = forms.HiddenInput()
        return form

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["all_catalog"] = Catalog.objects.all()
        return context
    

class CatalogBranchCreateView(CreateView):
    model = Catalog
    fields = ('name', 'parent')
    template_name = "catalogue/catalog_new_form.html"
    success_url = '/catalog/list/'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        p = Catalog.objects.get(id=self.kwargs.get("parent_id"))
        form.fields['parent'].initial = p
        return form
    

class CatalogUpdateView(UpdateView):
    model = Catalog
    fields = ('name', 'parent')
    template_name = "catalogue/catalog_form.html"
    success_url = '/catalog/list/'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        services = Service.objects.filter(category_id = self.object.id)
        context = super().get_context_data(**kwargs)
        context["service_list"] = services
        context["all_catalog"] = Catalog.objects.all()
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        form.fields['parent'].label = "Branch"
        return form


class SidebarListView(ListView):
    model = Catalog
    template_name = "catalogue/catalog_services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['un'] = None
        context['qs'] = None
        if self.request.user.is_authenticated:
            context['un'] = get_complete_name(self.request)
            if ShoppingCart.active_shoppingcart.filter(buyer=self.request.user):
                context['qs'] = ShoppingCart.active_shoppingcart.filter(buyer=self.request.user)

        catalog_w_services = Service.objects.all().values_list('category', flat=True).distinct()
        cs = list(catalog_w_services)
        for item in cs:
            c = Catalog.objects.get(id=item)
            if c.parent is not None:
                if c.parent.id not in cs:
                    cs.append(c.parent.id)
        
        catalog_with_services = Catalog.objects.filter(id__in=cs)
        context["catalog_items_with_services"] = catalog_with_services
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
        catalog_w_services = Service.objects.all().values_list('category', flat=True).distinct()
        cs = list(catalog_w_services)
        for item in cs:
            c = Catalog.objects.get(id=item)
            if c.parent is not None:
                if c.parent.id not in cs:
                    cs.append(c.parent.id)
        
        catalog_with_services = Catalog.objects.filter(id__in=cs)
        context["catalog_items_with_services"] = catalog_with_services
        context["services"] = services
        context["services_for_catalog_item"] = cat_obj
        context["catalog_list"] = cat_tree
        return context   


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ('name', 'category', 'cost', 'service_type', 'approval_type')
    template_name = "catalogue/service_form.html"
    success_url = '/catalog/list/'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         context = super().get_context_data(**kwargs)
    #     context["service_list"] = services
         context["all_catalog"] = Catalog.objects.all()
         return context
    
    # def get_form(self, form_class=None):
    #     form = super().get_form( form_class)
    #     form.fields['parent'].label = "Branch"
    #     return form