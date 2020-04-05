from rest_framework import serializers

from django.contrib.auth.models import User,Group
from .models import Charge, Category

class ChargeSerializer(serializers.ModelSerializer):
    item = serializers.CharField(max_length=20)
    type_name = serializers.CharField(max_length=20)
    date = serializers.DateTimeField()
    cost = serializers.DecimalField(max_digits=5, decimal_places=0)
    in_out_come = serializers.CharField(max_length=10)

    # def create(self, validated_data):
    #     return Charge.objects.create(**validated_data)

    class Meta:
        model = Charge
        fields = '__all__'
        # fields = ('item', 'type_name', 'date', 'cost', 'income_outcome')

class CategorySerializer(serializers.ModelSerializer):
    item_type = serializers.CharField(max_length=20)

    # def create(self, validated_data):
    #     # Category_Serializer = CategorySerializer(validated_data.get('item_type'))
    #     # Category_Serializer.save()
    #     return Category.objects.create(**validated_data)

    class Meta:
        model = Category
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         field = ['url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']