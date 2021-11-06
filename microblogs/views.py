from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from microblogs.models import User, Post
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


@login_required
def feed(request):
    logged_in_user = request.user
    posts = Post.objects.filter(author=logged_in_user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author = logged_in_user, text = form.cleaned_data.get('text'))
            return redirect('feed')
        messages.add_message(request, messages.ERROR, 'The provided post were invalid!')
    else:
        users = User.objects.all()
        form = PostForm()
    return render(request, 'feed.html', {'user': request.user, 'form': form, 'posts': posts})




def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        # If the log in was unsuccesfull
        messages.add_message(request, messages.ERROR, 'The credentials provided were invalid!')
    form = LogInForm()
    return render(request, 'log_in.html', {'form' : form})


def log_out(request):
    logout(request)
    return redirect('home')


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})



@login_required
def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(author=user)
    return render(request, 'show_user.html', {'user': user, 'posts': posts})
