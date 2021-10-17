from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from dsuser.decorators import login_required
from .models import Post
from dsuser.models import Dsuser
from .forms import PostForm
from tag.models import Tag

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'post.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

@method_decorator(login_required, name='dispatch')
class PostCreate(FormView):
    template_name = 'register_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        username = self.request.session.get('user')
        user = Dsuser.objects.get(username=username)
        tags = form.data.get('tags').split(',')
        post = Post()
        post.title = form.data.get('title')
        post.writer = user
        post.image_address = form.data.get('image_address')
        post.contents = form.data.get('contents')
        post.save()

        for tag in tags:
            if not tag:
                continue

            _tag, _ = Tag.objects.get_or_create(name=tag)
            post.tags.add(_tag)
        return super().form_valid(form)


class PostDetail(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'