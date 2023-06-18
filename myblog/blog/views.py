from django.shortcuts import render

# Create your views here.
from .models import Post
import requests
from bs4 import BeautifulSoup as bs


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})
from .forms import PostForm, JdForm

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., display it or perform other actions)
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # Add your desired logic here
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})

def apply(request):
    form = JdForm(request.POST or None)
    posts = {"username":"test user", "content":"I am a very experienced developer"}

    if form.is_valid():
        jd = form.cleaned_data.get('jd')
        return render(request, 'blog/apply.html', {'posts': posts, 'form': form, 'jd': jd})

    
    return render(request, 'blog/apply.html', {'posts': posts, 'form': form})


# def apply(request):
#     form = JdForm(request.POST or None)
    
#     if form.is_valid():
#         url = form.cleaned_data['url']
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             title = soup.title.string

#             posts = {
#                 'username': form.cleaned_data['username'],
#                 'content': form.cleaned_data['content'],
#                 'title': title
#             }
            
#             return render(request, 'blog/apply.html', {'posts': posts, 'form': form})
    
#     return render(request, 'blog/apply.html', {'form': form})
