from django.db.models import Count
from rest_framework import serializers

from .models import Resume


class ResumeBasicsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

    class Meta:
        model = Resume
        fields = ('__all__')
