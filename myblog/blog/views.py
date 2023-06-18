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
        url = form.cleaned_data.get('url')
        response = requests.get(url)
        
        
        if response.status_code == 200:
            soup = bs(response.text, 'html.parser')
            
            meta_tag = soup.find('meta', attrs={'name': 'title', 'property': 'og:title'})
            meta_tag2 = soup.find('meta', attrs={'name': 'description', 'property': 'og:description'})

            if meta_tag:
                title = meta_tag['content']
            
            content = meta_tag2['content']
            
            h2_elements = soup.find_all('h2')
            all_texts = []
            for h2_element in soup.strings:
                text = h2_element.get_text()
                all_texts.append(text)
            text = soup.get_text()
            jd = {
                'default': all_texts,
                'title': title,
                'content': response.text
            }
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
