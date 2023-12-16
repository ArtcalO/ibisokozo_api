
from django.contrib import admin
from django.urls import path, include,re_path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf.urls.static import static

from api.views import *
from . import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.SimpleRouter()





urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include(router.urls)),
    path('api/', include("api.urls")),
    path("graphql_api", include("graphql_api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', obtain_auth_token, name='obtain_auth_token'),

   
] 
