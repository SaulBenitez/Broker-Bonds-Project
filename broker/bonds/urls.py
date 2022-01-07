from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bonds import views

router = DefaultRouter()
# router.register('create', views.BondCreateGeneric)

urlpatterns = [
    # path('sell/', views.UserLoginApiView.as_view()),
    # path('buy/', views.UserSignUpAPIView.as_view()),
    # path('create/', views.BondCreateAPIView.as_view()),
    path('create/', views.BondCreateSellOrder.as_view()),
    path('list/', views.BondSellList.as_view()),
    # path('list/usd/', views.UserDetailAPIView.as_view()),
    path('', include(router.urls))
]