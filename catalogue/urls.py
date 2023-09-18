from django.urls import path

from catalogue.views import show_catalog, CatalogCreateView, CatalogUpdateView, SidebarListView, ServiceCreateView, ServiceListView

urlpatterns = [
    path('list/', show_catalog, name='show_catalog'),
    path('services/', SidebarListView.as_view(), name='show_sidebar'),
    path("create/add/", CatalogCreateView.as_view(), name='create_catalog'),
    path("update/<int:pk>/", CatalogUpdateView.as_view(), name='update_catalog'),
    path("services/<int:catalog_id>/", ServiceListView.as_view(), name='show_services'),
    path("service/create/<int:catalog_id>/", ServiceCreateView.as_view(), name='create_service'),
]