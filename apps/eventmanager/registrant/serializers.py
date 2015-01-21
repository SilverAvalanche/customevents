#serializers.py- Registrant
from rest_framework import serializers
from apps.eventmanager.registrant.models import *
from django.contrib.auth.models import User

class RegistrantSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='registrant-highlight', format='html')

    class Meta:
        model = Registrant
        fields = ('url', 'highlight', 'owner', 'code',
                  'linenos', 'language', 'style')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    registrants = serializers.HyperlinkedRelatedField(queryset=Registrant.objects.all(), 
                                                view_name='registrant-detail', many=True)
    model = User
    fields = ('url', 'username', 'registrant')
