from django import forms
from .models import Post, JdPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'content']

# class JdForm(forms.ModelForm):
#     class Meta:
#         model = JdPost
#         fields = ['username', 'jd']

class JdForm(forms.ModelForm):
    class Meta:
        model = JdPost
        fields = ['username', 'jd']
        labels = {
            'username': 'Username',
            'jd': 'Job Description',
        }