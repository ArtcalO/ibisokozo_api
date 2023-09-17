import graphene
from graphene_django import DjangoObjectType

from api.models import Igisokozo, InyishuIgisokozo

class IgisokozoType(DjangoObjectType):
    class Meta:
        model = Igisokozo
        fields = "__all__"
class InyishuIgisokozoType(DjangoObjectType):
    class Meta:
        model = InyishuIgisokozo
        fields = "__all__"

class Query(graphene.ObjectType):
    ibisokozo_vyose = graphene.List(IgisokozoType)
    inyishu_zyose = graphene.List(InyishuIgisokozoType)

    def resolve_ibisokozo_vyose(root, info):
        # We can easily optimize query count in the resolve method
        return Igisokozo.objects.all()

    def resolve_category_by_name(root, info, name):
        return InyishuIgisokozo.objects.select_related("igisokozo").all()

schema = graphene.Schema(query=Query)