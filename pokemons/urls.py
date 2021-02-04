from django.urls import path

from rest_framework import routers

from .views import PokemonsViewSet

router = routers.DefaultRouter()
router.register('pokemons', PokemonsViewSet)

urlpatterns = router.urls