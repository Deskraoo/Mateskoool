from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from blog.quickstart import views
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agrupacion_numerica', views.agrupacion_numerica, name='agrupacion_numerica'),
    path('clasificacion_numerica', views.agrupacion_numerica, name='clasificacion_numerica'),
    path('clasificacion_seriacion', views.clasificacion_seriacion, name='clasificacion_seriacion'),
    path('contacto', views.contacto, name='contacto'),
    path('figuras_geometricas', views.figuras_geometricas, name='figuras_geometricas'),
    path('multiplicacion_division', views.multiplicacion_division, name='multiplicacion_division'),
    path('numeros', views.numeros, name='numeros'),
    path('par_impar', views.par_impar, name='par_impar'),
    path('suma_resta', views.suma_resta, name='suma_resta'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^recover/(?P<signature>.+)/$', views.recover_done,
    name='password_reset_sent'),
    url(r'^recover/$', views.recover, name='password_reset_recover'),
    url(r'^reset/done/$', views.reset_done, name='password_reset_done'),
    url(r'^reset/(?P<token>[\w:-]+)/$', views.reset,
    name='password_reset_reset'),
]
