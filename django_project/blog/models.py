from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from promotion.models import Promotion



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    is_finished = models.BooleanField(default=False)
    
    user_limit = models.IntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(10)],
        default=2,
    )
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostMembers(models.Model):
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name='members'
    )

    users = models.ManyToManyField(
        User,
        related_name='posts_joined',
    )

    def __str__(self):
        return f'{self.post.title} {len(self.users.all())} / {self.post.user_limit}'


class Comment(models.Model):

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return f'{self.author.username} {self.post.title} {self.date_posted}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
