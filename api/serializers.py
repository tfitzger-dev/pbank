from django.contrib.auth.models import User

from rest_framework import serializers
from api.models import Bill

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ('url', 'id', 'amount', 'name', 'key', 'paid', 'due_day', 'owner')
        
    owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bills')
    bills = serializers.HyperlinkedRelatedField(many=True, view_name='bill-detail', read_only=True)