from django.contrib import admin
from django.urls import path, include
from twitter.views import PostView, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getPosts/', PostView),
    path('', include(router.urls)),
]
