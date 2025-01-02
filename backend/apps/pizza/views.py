from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from apps.pizza.filter import PizzaFilter
# from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    # queryset = PizzaModel.objects.less_than_size(100)

    queryset = PizzaModel.objects.all()
    # pagination_class = None
    filterset_class = PizzaFilter

    permission_classes = (IsAuthenticated,)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()

    http_method_names = ['get', 'put', 'patch', 'delete']

