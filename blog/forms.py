from django import forms
# from django.forms import ModelForm
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Blog.objects.filter(title__iexact = title)

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        if qs.exists():
            raise forms.ValidationError("Title Already Used")

        return title
