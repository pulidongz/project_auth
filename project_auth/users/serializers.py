from rest_framework import serializers
from users.models import HabUsers

class HabUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabUsers
        fields = '__all__'