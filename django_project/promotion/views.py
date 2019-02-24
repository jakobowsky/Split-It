from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.list import MultipleObjectMixin

from blog.models import Post
from .models import Brand, Promotion


class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion/promotions.html'
    context_object_name = 'promotions'
    ordering = ['-date_posted']
    paginate_by = 5


class BrandListView(ListView):
    model = Brand
    template_name = 'promotion/brands.html'
    context_object_name = 'brands'
    paginate_by = 5


class PromotionBrandListView(ListView, MultipleObjectMixin):
    model = Promotion
    template_name = 'promotion/brand_promotions.html'
    context_object_name = 'promotions'
    paginate_by = 5

    def get_queryset(self):
        brand = get_object_or_404(Brand, name=self.kwargs.get('brand'))
        return Promotion.objects.filter(brand=brand).order_by('-date_posted')


class PromotionDetailView(DetailView, MultipleObjectMixin):
    model = Promotion
    template_name = 'promotion/promotion_detail.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(promotion=self.get_object())
        context = super(PromotionDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context

