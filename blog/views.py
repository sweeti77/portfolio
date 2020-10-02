from django.shortcuts import get_object_or_404, render

from .models import Blog

# Create your views here.

def blogPage(request):
    blog_obj = Blog.objects.all()
    return render(request, 'blogPage.html', {'blogs':blog_obj, 'headline':"BLOGS"})

def blogDetail(request, blog_id):
    blogObj = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog':blogObj, 'headline':"BLOGS"})




