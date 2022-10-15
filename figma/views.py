from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserProfileForm, UserPostsForm
from django.contrib import messages
from .utils import user_registered, user_authenticated
from .models import User
# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if user_registered(request.POST['username']):
            if user_authenticated(request.POST['username'], request.POST['password']):
                request.session.__setitem__('uname', request.POST['username'])
                user = User.objects.get(username=request.POST['username'])
                return redirect(f'/userprofile{user.id}')
            return render(request, 'login_page.html', {'form': form, 'error': 'Invalid password'})
        return render(request, 'login_page.html', {'form': form, 'error': 'Username is not registered pls register first'})
    form = LoginForm()
    return render(request, "login_page.html", {'form': form})


def user_registeration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if not user_registered(uname=request.POST['username']):
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, f'{request.POST["username"]} is successfully registered')
                return redirect('/')
            return render(request, 'user_registeration_page.html', {'form': form, 'errors': form.errors})
        return render(request, 'user_registeration_page.html', {'form': form, 'msg': 'Username already exist pls try different username'})
    form = UserRegistrationForm()
    return render(request, 'user_registeration_page.html', {'form': form})


def user_profile(request, pk):
    if 'uname' in request.session:
        user = User.objects.get(id=pk)
        try:
            profile = user.profile
            proform = None
        except:
            proform = UserProfileForm()
            profile = None
        try:
            posts = user.posts.all().order_by('photo')
        except:
            posts = None
        return render(request, 'user_profile.html', {'form': proform, 'profile': profile, 'id': pk, 'posts': posts})
    return redirect('/')


def add_user_profile(request, pk):
    if 'uname' in request.session:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            user = User.objects.get(id=pk)
            if form.is_valid():
                prof = form.save(commit=False)
                prof.user = user
                prof.save()
                return redirect(f'/userprofile{pk}')
            errors = form.errors
            messages.add_message(request, messages.ERROR, errors)
            return redirect(f'/userprofile{user.id}')
    return redirect('/')


def update_user_profile(request, pk):
    if 'uname' in request.session:
        user = User.objects.get(id=pk)
        profile = user.profile
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
               form.save()
               return redirect(f'/userprofile{pk}')
            return render(request, 'user_profile_update.html', {'form': form, 'id': pk, 'errors': form.errors})
        form = UserProfileForm(instance=profile)
        return render(request, 'user_profile_update.html', {'form': form, 'id': pk})
    return redirect('/')


def post_upload(request, pk):
    if 'uname' in request.session:
        if request.method == 'POST':
            user = User.objects.get(id=pk)
            form = UserPostsForm(files=request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = user
                post.save()
                return redirect(f'/userprofile{pk}')
            return render(request, 'short_page.html', {'form': form, 'errors': form.errors, 'id': pk})
        form = UserPostsForm()
        return render(request, 'short_page.html', {'form': form, 'id': pk})
    return redirect('/')


def logout(request):
    if 'uname' in request.session:
        del request.session['uname']
    return redirect('/')
