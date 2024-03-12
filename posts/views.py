from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.utils import timezone


def view_posts(request):
    posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'posts/view_posts.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('view_posts')
    else:
        form = BlogPostForm()
    return render(request, 'posts/add_post.html', {'form': form})