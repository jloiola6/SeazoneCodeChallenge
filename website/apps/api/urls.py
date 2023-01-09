
# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers
 
# import everything from views
from apps.api.views import *
 
# define the router
router = routers.DefaultRouter()
 
# # define the router path and viewset to be used
router.register('imoveis', ImovelViewSet)
router.register('anuncios', AnuncioViewSet)
router.register('reservas', ReservaViewSet)
 
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]