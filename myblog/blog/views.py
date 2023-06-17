from django.shortcuts import render

# Create your views here.
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})
from .forms import PostForm

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
