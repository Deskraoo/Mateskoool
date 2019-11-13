from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.agrupacion_numerica, name='agrupacion_numerica'),
    path('', views.clasificacion_seriacion, name='clasificacion_seriacion'),
    path('', views.contacto, name='contacto'),
    path('', views.figuras_geometricas, name='figuras_geometricas'),
    path('', views.multiplicacion_division, name='multiplicacion_division'),
    path('', views.numeros, name='numeros'),
    path('', views.par_impar, name='par_impar'),
    path('', views.suma_resta, name='suma_resta'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
