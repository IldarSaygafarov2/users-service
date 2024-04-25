from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer, UpdateUserSerializer, ChangePasswordSerializer
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

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'update':
            return UpdateUserSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer