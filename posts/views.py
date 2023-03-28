from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import SearchForm
from accounts.models import Account
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_post.html'
    form_class = PostForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class PostView(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        subscribe_to = request.GET.get('subscribe_to')
        if subscribe_to:
            request.user.subscriptions.add(subscribe_to)
        subscribe_of = request.GET.get('subscribe_of')
        if subscribe_of:
            request.user.subscriptions.remove(subscribe_of)
        like = request.GET.get('like')
        if like:
            request.user.liked_posts.add(like)
        unlike = request.GET.get('unlike')
        if unlike:
            request.user.liked_posts.remove(unlike)
        self.extra_context = {'comment_form': CommentForm(), 'search_form': SearchForm()}
        return super().get(request, *args, **kwargs)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user_pk = kwargs.get('upk')
        post_pk = kwargs.get('pk')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = get_object_or_404(Account, pk=user_pk)
            comment.post = get_object_or_404(Post, pk=post_pk)
            comment.save()
            return redirect('profile_post', user_pk, post_pk)
        return redirect('profile_post', user_pk, post_pk)
