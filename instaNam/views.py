from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PostForm, UserForm
from .models import Post
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })


@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', pk = post.pk)
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post' : post})



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        error = "아이디가 이미 존재합니다."
        return render(request, 'registration/signup.html', {'form': form}, {'error': error})