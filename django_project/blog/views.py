from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView
)
from django.views.generic.list import MultipleObjectMixin

from promotion.models import Promotion
from .models import Post, Comment
from .forms import CommentForm
# from promotion.models import Promotion

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['promotions'] = Promotion.objects.all()[:5]
    #     return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# class PostDetailView(FormView, DetailView):
#     model = Post
#     form_class = CommentForm

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class PostDetailView(DetailView, MultipleObjectMixin):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Comment.objects.filter(post=self.get_object())
        context = super(PostDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        context['form'] = CommentForm

        return context


class MyFormView(FormView):
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', ]

    ''' Very important and useful 
    # def get_initial(self):
    #     initial = super().get_initial()
    #     # cpf - it's the name of the field on your current form
    #     # self.args will be filled from URL. I'd suggest to use named parameters
    #     # so you can access e.g. self.kwargs['cpf_initial']
    #     initial['promotion'] = self.kwargs['promotion_id'] 
    #     return initial
    '''

    def get_context_data(self, *args, **kwargs):
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context['promotion'] = get_object_or_404(
            Promotion, pk=self.kwargs['promotion_id'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.promotion = get_object_or_404(
            Promotion, pk=self.kwargs['promotion_id'])
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def get_context_data(self, *args, **kwargs):
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context['promotion'] = get_object_or_404(
            Promotion, pk=self.kwargs['promotion_id'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.promotion = get_object_or_404(
            Promotion, pk=self.kwargs['promotion_id'])
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    #    success_url = '/'

    def get_success_url(self):
        comment = get_object_or_404(
            Comment, pk=self.kwargs['pk'])
        return reverse_lazy('post-detail', kwargs={'pk': comment.post.id})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
