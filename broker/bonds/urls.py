from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bonds import views

router = DefaultRouter()
# router.register('create', views.BondCreateGeneric)

urlpatterns = [
    path('user/own/', views.BondUserList.as_view()),
    path('user/sale/', views.BondSaleOrderUserList.as_view()),
    path('user/buy/', views.BondBuyOrderUserList.as_view()),
    path('create/', views.BondCreateSaleOrder.as_view()),
    path('sale/', views.BondForSaleList.as_view()),
    path('buy/<int:pk>', views.BondBuyOrder.as_view()),
    path('sale/usd/', views.BondForSaleOrderListUSD.as_view()),
    path('sale/usdinfo/', views.BondDollarInfo.as_view()),
    path('', include(router.urls))
]