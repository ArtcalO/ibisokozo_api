from rest_framework import serializers
from .models import *

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

class LebonCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = LebonCoin
        fields = "__all__"