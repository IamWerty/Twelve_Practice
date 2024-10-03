from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reviews:list')
    else:
        form = UserCreationForm()
    return render(request, 'reviews_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reviews:list')
    else:
        form = AuthenticationForm()
    return render(request, 'reviews_app/login.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_app/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews:list')
    else:
        form = ReviewForm()
    return render(request, 'reviews_app/add_review.html', {'form': form})