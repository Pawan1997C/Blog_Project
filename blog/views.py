from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterFrorm, UserUpdateForm, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Create your views here.

class PostListView(ListView):
    login_url = 'login'
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(title__icontains=query).order_by('-date_posted')
        else:
            object_list = self.model.objects.all().order_by('-date_posted')
        return object_list

class PostDetailView(DetailView):
    login_url = 'login'
    model = Post


class UserPostListView(ListView):
    login_url = 'login'
    model = Post
    template_name = 'blog/user_posts.html'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostByCategoryListView(ListView):
    login_url = 'login'
    model = Post
    template_name = 'blog/post_by_category.html'
    paginate_by = 5


    def get_queryset(self):
        category = get_object_or_404(Category, name = self.kwargs.get('category'))
        return Post.objects.filter(category = category).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    model = Post
    fields = ['title', 'content', 'image', 'category']
    success_message = 'Post Created Successfully!!'
    success_url = reverse_lazy('blog-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Post
    fields = ['title', 'content','image', 'category']
    success_url = reverse_lazy('blog-home')
    success_message = 'Post Updated Succesfully!!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Post
    success_message = 'Post Deleted Successfully!!'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required(login_url = 'login')
def about(request):
    return render(request, 'blog/about.html')


def register(request):
    if request.user.is_authenticated:
        messages.success(request, 'You"re Logged In')
        return redirect('blog-home')
    else:
        if request.method == 'POST':
            form = UserRegisterFrorm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account Created for {username}')
                return redirect('login')
        else:
            form = UserRegisterFrorm()
        return render(request, 'user/register.html', {'form': form})


@login_required(login_url = 'login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Updated Successfully!!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = UserProfileUpdateForm(instance = request.user.profile)
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'user/profile.html', context)