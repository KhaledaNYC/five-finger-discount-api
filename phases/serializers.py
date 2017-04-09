from rest_framework import serializers
from phases.models import Phase


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ('winner','game')
