from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('list/', views.UserList.as_view(), name='users_list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]