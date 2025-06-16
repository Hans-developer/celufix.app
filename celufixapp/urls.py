from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('telefonos/<int:marca_id>', views.telefonos, name='telefonos'),
    path('repuestos/<int:telefono_id>/', views.repuestos, name='repuestos'),

]