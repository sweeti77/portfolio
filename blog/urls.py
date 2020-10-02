from django.urls import include, path

from .views import *

urlpatterns = [
    path('', blogPage, name="blogPage"),
    path('<int:blog_id>', blogDetail, name="blogDetail")
]
