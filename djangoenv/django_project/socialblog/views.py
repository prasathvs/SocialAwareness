from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.dates import YearArchiveView

def index(request):
    return render(request, 'Socialblog/index.html')

def business(request):
    context = {

        'posts': Post.objects.all()

    }
    return render(request, 'Socialblog/business.html', context)
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'Socialblog/business.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "date_posted"
    make_object_list = True
    allow_future = True

def about(request):
    return render(request, 'Socialblog/about.html')


