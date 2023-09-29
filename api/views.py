from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *

class IgisokozoViewSet(viewsets.ModelViewSet):
    queryset = Igisokozo.objects.all()
    serializer_class = IgisokozoSerializer
    permission_classes = [AllowAny]

class InyishuIgisokozoViewSet(viewsets.ModelViewSet):
    queryset = InyishuIgisokozo.objects.all()
    serializer_class = InyishuIgisokozoSerializer
    permission_classes = [AllowAny]

class IbisokozoCollectedViewSet(viewsets.ModelViewSet):
    queryset = IbisokozoCollected.objects.all()
    serializer_class = IbisokozoCollectedSerializer
    permission_classes = [AllowAny]
