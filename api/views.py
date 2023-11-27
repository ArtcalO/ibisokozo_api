from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User





class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
