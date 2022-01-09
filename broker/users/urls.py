from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

router = DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('signup/', views.UserSignUpAPIView.as_view()),
    path('<int:pk>/', views.UserDetailAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]