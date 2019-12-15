from rest_framework import serializers

from team_manager.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'timestamp'
        ]
