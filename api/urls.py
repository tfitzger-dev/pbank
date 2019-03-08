from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bills', views.BillViewSet)
router.register(r'accounts', views.BankAccountViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'transactions', views.TransactionViewSet)

schema_view = get_schema_view(title='PBank API')

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),    
]