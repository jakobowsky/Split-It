from django.urls import path
from .views import (
    PromotionListView,
    PromotionBrandListView
)

urlpatterns = [
    path('', PromotionListView.as_view(), name='promotion-home'),
    path('brands/<str:brand>', PromotionBrandListView.as_view(), name='promotion-brand'),    
]

