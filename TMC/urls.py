from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'Orden', views.OrdenesViewSet)
router.register(r'Cliente', views.ClientesViewSet)
router.register(r'Tecnico', views.TecnicosViewSet)

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

#urlpatterns = [
#    path('', views.post_list, name='post_list'),
#    url(r'^api-auth/', include('rest_framework.urls')),
#]
