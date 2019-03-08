from django.contrib.auth.models import User

from rest_framework import serializers
from api.models import Bill, BankAccount, Institution, Transaction


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


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ('url', 'id', 'owner', 'name')
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)


class BankAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('url', 'id', 'owner', 'institution', 'short_name', 'full_name', 'type', 'balance')
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('url', 'id', 'account', 'name', 'amount', 'date')
