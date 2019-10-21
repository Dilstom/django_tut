from rest_framework import serializers, viewsets
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()