from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from ..services.mixins import *
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy


def posts_list(request, page):
    posts = Post.objects.all()
    paginator = Paginator(posts, per_page=2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'page_obj': page_object}
    return render(request, 'blog/post_func_list.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная станица'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class PostBySubjectListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    subject = None

    def get_queryset(self):
        self.subject = Subject.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.all().filter(subject__slug=self.subject.slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статьи из категории: {self.subject.subject_name}'
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление поста'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(AuthorRequiresMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    form_class = PostUpdateForm
    login_url = 'home'
    success_message = 'Материал был успешно обновлен'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление статьи: {self.object.title}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostDeleteView(AuthorRequiresMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление статьи: {self.object.title}'
        return context
