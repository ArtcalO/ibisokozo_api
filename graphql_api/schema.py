import graphene
from graphene_django import DjangoObjectType

from api.models import Igisokozo, InyishuIgisokozo

class IgisokozoType(DjangoObjectType):
    class Meta:
        model = Igisokozo
        fields = ("id", "igisokozo", "itariki")

class InyishuIgisokozoType(DjangoObjectType):
    class Meta:
        model = InyishuIgisokozo
        fields = ("id", "igisokozo","inyishu", "itariki")

class Query(graphene.ObjectType):
    ibisokozo_vyose = graphene.List(IgisokozoType)
    inyishu_zyose = graphene.List(InyishuIgisokozoType)

    def resolve_ibisokozo_vyose(root, info):
        return Igisokozo.objects.all()

    def resolve_inyishu_zyose(root, info):
        return InyishuIgisokozo.objects.select_related("igisokozo").all()

schema = graphene.Schema(query=Query)