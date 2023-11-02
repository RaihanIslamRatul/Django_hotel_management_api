from rest_framework import serializers
from .models import *



class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'

    # def validate(self, data):
    #     if data['name']:
    #         for n in data['name']:
    #             if n.isdigit():
    #                 raise serializers.ValidationError({'error': 'name can not contains digit'})

    #     return data