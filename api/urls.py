from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('users', views.UserViewSet, basename='user')

urlpatterns = router.urls
urlpatterns += [path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password')]