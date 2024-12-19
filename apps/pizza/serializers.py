from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
        class Meta:
                model = PizzaModel
                # fields = ('id', 'name', 'price', 'created_at', 'updated_at')
                fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=20)
    # size = serializers.IntegerField()
    # price = serializers.FloatField()
    #
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     pizza = PizzaModel.objects.create(**validated_data)
    #     print(pizza)
    #     return pizza
    #
    # def update(self, instance, validated_data:dict):
    #     for k, v in validated_data.items():
    #         setattr(instance, k, v)
    #     instance.save()
    #     return instance
