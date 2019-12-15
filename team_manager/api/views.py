from rest_framework import generics

from team_manager.models import Team
from .serializers import TeamSerializer

class TeamAPIView(generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = TeamSerializer
    queryset            = Team.objects.all()

