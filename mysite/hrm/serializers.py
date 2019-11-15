from rest_framework import serializers
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):
    job_seeker_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)
    class Meta:
        model = Users
        # fields = ('name', 'job_seeker_id')
        fields = '__all__'
