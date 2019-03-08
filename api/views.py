from django.contrib.auth.models import User, AnonymousUser
from api.models import Bill
from api.serializers import UserSerializer, BillSerializer
from api.permissions import IsOwner
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bills': reverse('bill-list', request=request, format=format),
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
