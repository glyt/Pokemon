from rest_framework.viewsets import ModelViewSet

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonsViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
