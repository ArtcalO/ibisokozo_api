from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
       
class UserRegistrationSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'groups']  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': True}}  # Ensure that the password field is write-only

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user = CustomUser.objects.create_user(**validated_data)
        
        # Set groups using the set() method
        user.groups.set(groups_data)
        
        return user
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