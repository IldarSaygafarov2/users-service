from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet


# class UserList(generics.ListAPIView):
#     """
#     Returns a list of all users
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
#     search_fields = ['username']
#     ordering_fields = ['username', 'email']
#
#
# class UserCreateView(generics.CreateAPIView):
#     """
#     Creating a new user
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserRetrieveView(generics.RetrieveAPIView):
#     """
#     Retrieving user by pk
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDeleteView(generics.DestroyAPIView):
#     """
#     Delete user by pk
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserUpdateView(generics.UpdateAPIView):
#     """
#     Update user by pk
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['username']
    ordering_fields = ['username', 'email']
