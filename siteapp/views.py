from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
# Create your views here.
def home(request):
  return render(request,'home.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def create(request):
  if request.method=="POST":
    post = Post()
    post.image = request.FILES['image']
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})