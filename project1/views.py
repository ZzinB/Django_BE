from django.shortcuts import render, redirect
from siteapp.models import Post

def create(request):
  if request.method=="POST":
    post = Post()
    post.image = request.FILES['image']
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})