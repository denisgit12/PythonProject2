from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer

from rest_framework.request import Request

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
#
# class PizzaListCreateView(APIView):
#     def get(self,request:Request, *args, **kwargs):
#         # pizzas = PizzaModel.objects.all()
#         # pizzas = pizzas.filter(price__gt=101)
#
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response('not found', status=status.HTTP_404_NOT_FOUND)
#
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response('not found', status=status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         serializer = PizzaSerializer(pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             pizza = PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response('not found', status=status.HTTP_404_NOT_FOUND)
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        request:Request = self.request
        return filter_pizza(request.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()

    http_method_names = ['get', 'put', 'patch', 'delete']

