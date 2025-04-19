from django.contrib import admin
from django.urls import path, include
from twitter.views import PostView, PostViewSet, UserViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getPosts/', PostView),
    path('', include(router.urls)),
]
