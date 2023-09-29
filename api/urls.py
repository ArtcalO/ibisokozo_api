from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register("ibisokozo", IgisokozoViewSet)
router.register("inyishu-igisokozo", InyishuIgisokozoViewSet)
router.register("collect", IbisokozoCollectedViewSet)

urlpatterns = [
    path('',include(router.urls)),
]