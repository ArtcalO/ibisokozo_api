import random
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.core.cache import cache



correct_answer=None


#get connected user infos
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    
#get users' list 
class UsersListViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]



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
    
    
class IkibazoViewSet(viewsets.ModelViewSet):
    queryset = Ikibazo.objects.all()
    serializer_class = IkibazoSerializer
    permission_classes = [AllowAny]
    
class InyishuViewSet(viewsets.ModelViewSet):
    queryset = Inyishu.objects.all()
    serializer_class = InyishuSerializer
    permission_classes = [AllowAny]



class RandomIkibazoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IkibazoSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        random_ikibazo = random.choice(Ikibazo.objects.all())
        cache.set('correct_answer', random_ikibazo.inyishu.inyishu)

        correct_answer = random_ikibazo.inyishu.inyishu

        incorrect_answers = Ikibazo.objects.exclude(id=random_ikibazo.id).order_by('?')[:3]
        incorrect_answers = [incorrect.inyishu.inyishu for incorrect in incorrect_answers]

        options = [correct_answer] + incorrect_answers
        print(correct_answer)
        

        random.shuffle(options)

        serializer = self.get_serializer(random_ikibazo)
        data = serializer.data
        data['options'] = options

        return Response(data)
    
    
class CheckAnswerViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def check_answer(self, request):
        correct_answer = cache.get('correct_answer')
        selected_answer = request.data.get('selected_answer')
        print(correct_answer, selected_answer)

        user = self.request.user if self.request.user.is_authenticated else None

        response_data = {}
        

        if user:
            if selected_answer == correct_answer:
                user.score += 1
                user.save()

                response_data = {'result': 'Correct!', 'score': user.score}
            else:
                response_data = {'result': 'Incorrect. Try again!', 'score': user.score}
        else:
            response_data = {'result': 'User not authenticated.', 'score': 0}
            
            if selected_answer == correct_answer:

                response_data = {'result': 'Correct!, please authenticate to save your score'}
            else:
                response_data = {'result': 'Incorrect. Try again!, please authenticate to save your score'}

        return Response(response_data, status=status.HTTP_200_OK)

