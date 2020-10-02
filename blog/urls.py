from django.urls import include, path

from .views import *

urlpatterns = [
    path('', blogPage, name="blogPage"),
    path('<int:blog_id>', blogDetail, name="blogDetail"),
    path('create', blogCreate, name="blogCreate"),
    path('update/<int:blog_id>', blogUpdate, name="blogUpdate"),
    path('delete/<int:blog_id>', blogDelete, name="blogDelete"),

]
