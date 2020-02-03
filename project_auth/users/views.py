from users.models import HabUsers
from users.serializers import HabUsersSerializer
from rest_framework import generics

class HabUsersListCreate(generics.ListCreateAPIView):
    queryset = HabUsers.objects.all()
    serializer_class = HabUsersSerializer