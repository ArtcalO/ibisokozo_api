from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphql_api.schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path("", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]