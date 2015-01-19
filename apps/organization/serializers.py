from django.contrib.auth.models import User
from rest_framework import serializers
from apps.organization.models import Organization
from apps.organization.season import Season


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='organization-highlight', format='html')
    
    class Meta:
        model = Organization
        fields = ('url','highlight','owner','title','code','linenos','language','style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    organizations = serializers.HyperlinkedRelatedField(queryset=Organization.objects.all(), view_name='organization-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'organizations')

  

