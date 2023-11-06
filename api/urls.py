from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserRetrieveView.as_view(), name='user-detail'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
]


