from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/create/', views.UserCreateView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveView.as_view()),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view()),
]
