from django.urls import path

from .views import (
    Home,
    About,
    Tdca,
    Cawsdc,
    Nba,
    Bh,
    Chs,
    Cpcd,
    Ca,
    ProductDetails,
    CategoryDetails,
    ProductList,
    SearchProducts
)

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('about/',About.as_view(), name='about'),
    path('tdca/',Tdca.as_view(), name='tdca'), # 三角台曆區
    path('cawsdc/',Cawsdc.as_view(), name='cawsdc'), # 中西式桌曆
    path('nba/',Nba.as_view(), name='nba'), # 便條盒區
    path('bh/',Bh.as_view(), name='bh'), # 工商手冊
    path('chs/',Chs.as_view(), name='chs'), # 年曆掛軸
    path('cpcd/',Cpcd.as_view(), name='cpcd'), # 日曆 農民曆區
    path('ca/',Ca.as_view(), name='ca'), # 月曆區
    path('product-details/<str:slug>/',ProductDetails.as_view(), name='product-details'),
    path('category-details/<str:slug>/',CategoryDetails.as_view(), name='category-details'),
    path('product-list/',ProductList.as_view(), name='product-list'),
    path('search-products/',SearchProducts.as_view(), name='search-products'),
]