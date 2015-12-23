#-*- coding: UTF8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponse
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def hello(request):
	posts = Post.objects.all()
	return render(request, 'hi.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_list.html', {'post':post})

def post_new(request):
    print 'post_new'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('FirstExample.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
	print 'post_edit'
	post = get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('FirstExample.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form':form})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	Post.objects.filter(published_date = post.published_date ).delete()
	posts = Post.objects.all()	
	return render(request, 'hi.html', {'posts':posts})
