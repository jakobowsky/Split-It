from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Promotion

class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion/promotions.html'
    context_object_name = 'promotions'
    # ordering = ['-']
    paginate_by = 5

    