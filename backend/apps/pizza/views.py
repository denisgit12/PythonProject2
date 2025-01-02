from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request

from apps.pizza.filter import PizzaFilter
# from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer, PizzaPhotoSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    # queryset = PizzaModel.objects.less_than_size(100)

    queryset = PizzaModel.objects.all()
    # pagination_class = None
    filterset_class = PizzaFilter

    permission_classes = (AllowAny,)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()

    http_method_names = ['get', 'put', 'patch', 'delete']


class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny,)

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)

