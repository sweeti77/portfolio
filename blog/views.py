from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required

from .models import Blog

from .forms import BlogForm

# Create your views here.

def blogPage(request):
    blog_obj = Blog.objects.all()
    return render(request, 'blogPage.html', {'blogs':blog_obj, 'headline':"BLOGS"})

def blogDetail(request, blog_id):
    blogObj = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog':blogObj, 'headline':"BLOGS"})

@staff_member_required
def blogCreate(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        form = BlogForm()
    return render(request, 'blog/form.html', {'form':form, 'headline':"BLOGS"})

@staff_member_required
def blogUpdate(request, blog_id):
    blogObj = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST or None, instance=blogObj)
    if form.is_valid():
        form.save()
        return redirect('/blog')
    return render(request, 'blog/form.html', {'form':form, 'headline':"BLOGS"})


@staff_member_required
def blogDelete(request, blog_id):
    blogObj = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blogObj.delete()
        return redirect('/blog')

    return render(request, 'blog/delete.html', {'blog':blogObj, 'headline':"BLOGS"})



