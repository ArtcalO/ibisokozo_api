from rest_framework import serializers

class IgisokozoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Igisokozo
        fields = "__all__"

class InyishuIgisokozoSerializer(serializers.ModelSerializer):
    igisokozo = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='inyishu-igisokozo'
    )
    class Meta:
        model = InyishuIgisokozo
        fields = "__all__"