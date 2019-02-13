from django.urls import path
from .views import (
    PromotionListView,
    PromotionBrandListView,
    PromotionDetailView
)

urlpatterns = [
    path('', PromotionListView.as_view(), name='promotion-home'),
    path('detail/<int:pk>', PromotionDetailView.as_view(), name='promotion-detail'),
    path('brands/<str:brand>', PromotionBrandListView.as_view(), name='promotion-brand'),
]

