from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# DahliasInstitute2022
def CreateUser(data):
    print(data)
    try:
        user = User.objects.create_user(**data)
    except NameError:
        print(NameError)
    return user

@api_view(['GET', 'POST', 'Delete', 'PATCH'])
def PostView(request):
    if request.method == 'POST':
        # Create a new post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        # Retrieve all posts
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post = Post.objects.get(id=request.query_params.get('id'))
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    elif request.method == 'PATCH':
        try:
            post = Post.objects.get(id=request.query_params.get('id'))
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'error': 'Object not found'}, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        self.queryset.create(title=request.data['title'], 
                             content=request.data['content'],
                             owner=request.user)
        return Response({'message': 'Post created'}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = CreateUser(request.data)
        if user is not None:
            return Response({'user': user.username}, status=status.HTTP_201_CREATED)
        return Response({'error': 'User not created'}, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    