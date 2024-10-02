"""
URL configuration for drf_board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

# 맨 뒤 슬래시 제거
class CustomSimpleRouter(SimpleRouter): 
    def __init__(self):
        super().__init__(trailing_slash=False)  # 슬래시를 없앰

router = CustomSimpleRouter()
router.register('board', BoardViewSet)

urlpatterns = [
    #path('', BoardViewSet.as_view()),
    #path('<int:pk>', BoardViewSet.as_view()),
    path('', include(router.urls)),
]

