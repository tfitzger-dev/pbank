from django.contrib.auth.models import User, AnonymousUser
from api.models import Bill, BankAccount, Institution, Transaction
from api.serializers import UserSerializer, BillSerializer, BankAccountSerializer, InstitutionSerializer, TransactionSerializer
from api.permissions import IsOwner, IsOwnerOfAccount
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bills': reverse('bill-list', request=request, format=format),
        'accounts': reverse('account-list', request=request, format=format),
        'institutions': reverse('institution-list', request=request, format=format),
        'transactions': reverse('transaction-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsOwner,)
    
    def get_queryset(self):
        user = self.request.user
        return Bill.objects.filter(owner=user) if not isinstance(user, AnonymousUser) else None
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Institution.objects.filter(owner=user) if not isinstance(user, AnonymousUser) else None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return BankAccount.objects.filter(owner=user) if not isinstance(user, AnonymousUser) else None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOfAccount,)

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(account__owner=user) if not isinstance(user, AnonymousUser) else None

