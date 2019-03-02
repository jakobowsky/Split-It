from django.urls import path
from .views import (
    PromotionListView,
    PromotionBrandListView,
    PromotionDetailView,
    BrandListView,
    PromotionCategoryListView
)

urlpatterns = [
    path('', PromotionListView.as_view(), name='promotion-home'),
    path('detail/<int:pk>', PromotionDetailView.as_view(), name='promotion-detail'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/<str:brand>', PromotionBrandListView.as_view(), name='promotion-brand'),
    path('<str:category>/', PromotionCategoryListView.as_view(), name='promotion-category'),
]

