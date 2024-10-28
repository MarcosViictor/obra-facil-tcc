from django.contrib.auth import views as auth_views
from django.urls import path

from obras.views.consumoMaterial import ConsumoMaterialCreateView
from obras.views.dashboard import dashboard_obra
from usuarios.views import views
#Obras
from .views.obras import (ObraListView, ObraDetailView, ObraCreateView, 
    ObraUpdateView, ObraDeleteView
)
#funcionarios
from .views.funcionarios import  ProfissionalListView, ProfissionalDetailView,ProfissionalCreateView, ProfissionalUpdateView, ProfissionalDeleteView
#Acompanhamentos
from .views.acompanhamento import(
    AcompanhamentoListView,
    AcompanhamentoDetailView,
    AcompanhamentoCreateView,
    AcompanhamentoUpdateView,
    AcompanhamentoDeleteView
)
# Dashboard

#Materiai
from .views.materiais import(
    MaterialListView, MaterialDetailView, MaterialCreateView,
    MaterialUpdateView, MaterialDeleteView
)

#home
from .views.home import home
#logout
from .views.logout import logout_view

urlpatterns = [
    #home
    path('home/', home, name='home'),
    #
    #logout
    path('logout/', logout_view, name='logout'),
    #Obras
    path('listar/obras/', ObraListView.as_view(), name='obra-list'),
    path('<int:pk>/', ObraDetailView.as_view(), name='obra-detail'),
    path('create/', ObraCreateView.as_view(), name='obra-create'),
    path('<int:pk>/update/', ObraUpdateView.as_view(), name='obra-update'),
    path('<int:pk>/delete/', ObraDeleteView.as_view(), name='obra-delete'),
    #Funcionarios
    path('profissionais/', ProfissionalListView.as_view(), name='profissional-list'),
    path('profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional-detail'),
    path('profissionais/create/', ProfissionalCreateView.as_view(), name='profissional-create'),
    path('profissionais/<int:pk>/update/', ProfissionalUpdateView.as_view(), name='profissional-update'),
    path('profissionais/<int:pk>/delete/', ProfissionalDeleteView.as_view(), name='profissional-delete'),
    #Acompanhamentos
    path('acompanhamentos/', AcompanhamentoListView.as_view(), name='acompanhamento-list'),
    path('acompanhamentos/<int:pk>/', AcompanhamentoDetailView.as_view(), name='acompanhamento-detail'),
    path('acompanhamentos/create/', AcompanhamentoCreateView.as_view(), name='acompanhamento-create'),
    path('acompanhamentos/<int:pk>/update/', AcompanhamentoUpdateView.as_view(), name='acompanhamento-update'),
    path('acompanhamentos/<int:pk>/delete/', AcompanhamentoDeleteView.as_view(), name='acompanhamento-delete'),
    #dashboard
    path('dashboard/obra/<int:obra_id>/', dashboard_obra, name='dashboard-obra'),
    #materiais
    path('materiais/', MaterialListView.as_view(), name='material-list'),
    path('materiais/<int:pk>/', MaterialDetailView.as_view(), name='material-detail'),
    path('materiais/create/', MaterialCreateView.as_view(), name='material-create'),
    path('materiais/<int:pk>/update/', MaterialUpdateView.as_view(), name='material-update'),
    path('materiais/<int:pk>/delete/', MaterialDeleteView.as_view(), name='material-delete'),
    path('consumos/novo/', ConsumoMaterialCreateView.as_view(), name='consumo-create')

]
