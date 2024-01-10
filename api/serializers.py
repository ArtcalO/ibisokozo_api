from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['score']
       
class UserRegistrationSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'groups'] 
        extra_kwargs = {'password': {'write_only': True}}  
    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user = CustomUser.objects.create_user(**validated_data)
        
        user.groups.set(groups_data)
        
        return user
 
 
 
class InyishuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inyishu
        fields = ['id', 'inyishu', 'itariki']

        
        
 
 
#*For create

# class IkibazoSerializer(serializers.ModelSerializer):
#     inyishu = serializers.PrimaryKeyRelatedField(
#         queryset=Inyishu.objects.all(),
#         write_only=False,
#     )

#     class Meta:
#         model = Ikibazo
#         fields = ['id', 'igisokozo', 'itariki', 'inyishu']

#     def create(self, validated_data):
#         inyishu = validated_data.pop('inyishu')

#         # Create the Ikibazo instance
#         ikibazo_instance = Ikibazo.objects.create(
#             igisokozo=validated_data['igisokozo'],
#             itariki=validated_data.get('itariki'),
#             inyishu=inyishu,
#         )

#         return ikibazo_instance


#*For display
class IkibazoSerializer(serializers.ModelSerializer):
    inyishu = serializers.StringRelatedField()

    class Meta:
        model = Ikibazo
        fields = ['id', 'igisokozo', 'itariki', 'inyishu']

    def create(self, validated_data):
        inyishu = validated_data.pop('inyishu')

        # Create the Ikibazo instance
        ikibazo_instance = Ikibazo.objects.create(
            igisokozo=validated_data['igisokozo'],
            itariki=validated_data.get('itariki'),  # Assuming 'itariki' is optional
            inyishu=inyishu,
        )

        return ikibazo_instance







    
    
class IgisokozoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Igisokozo
        fields = "__all__"

class InyishuIgisokozoSerializer(serializers.ModelSerializer):
    igisokozo = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='igisokozo-detail'
    )
    class Meta:
        model = InyishuIgisokozo
        fields = "__all__"

class IbisokozoCollectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = IbisokozoCollected
        fields = "__all__"