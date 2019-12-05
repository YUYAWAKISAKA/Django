from django.shortcuts import render
# myblog/blogs/views.py
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
 
@login_required 
def index(request):
    return HttpResponse("Home")
 
@login_required  
def detail(request, pk):
    return HttpResponse("Post %s" % pk)
 
@login_required  
def create(request):
    return HttpResponse("Add New Post")
 
@login_required  
def update(request, pk):
    return HttpResponse("Edit Post %s" % pk)
 
@login_required  
def delete(request, pk):
    return HttpResponse("Delete Post %s" % pk)
