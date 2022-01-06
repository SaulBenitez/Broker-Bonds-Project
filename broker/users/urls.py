from django.urls import path, include
from users import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('signup/', views.UserSignUpAPIView.as_view()),
    path('<int:pk>/', views.UserDetailAPIView.as_view()),
    path('', include(router.urls))
]