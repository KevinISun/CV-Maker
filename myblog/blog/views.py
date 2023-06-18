from django.shortcuts import render, redirect

# Create your views here.
import os
import openai
from .models import Post
from .forms import PostForm, JdForm

openai.api_key = os.getenv('OPENAI_API_KEY')

user_data_dict = {}


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., display it or perform other actions)
            username = form.cleaned_data['username']
            content = form.cleaned_data['content']
            # Add your desired logic here

            # Can remove when database is set up
            if username in user_data_dict:
                user_data_dict[username] = user_data_dict[username] + [content]
            else:
                user_data_dict[username] = [content]
            
            return redirect('/apply')

    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})

# combine it with jd data and pass it to chatGPT

def generate_resume(job_description, username):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # Assuming you want to use the ChatGPT model
        messages=[
            {"role": "system", "content": "You are a skilled professional creating an English resume based on a job description and your client's personal information."},
            {"role": "user", "content": f"Job description: {job_description}; Personal information: {user_data_dict[username]}"},
        ],
    )   

    return response['choices'][0]['message']['content']



def apply(request):
    form = JdForm(request.POST or None)
    posts = {"username":"test user", "content":"I am a very experienced developer"}
    resume = ""

    if form.is_valid():
        jd = form.cleaned_data.get('jd')
        username = form.cleaned_data.get('username')
        # use username to retrieve user information 
        # store it and pass it to generate_resume function
        resume = generate_resume(jd, username)
        return render(request, 'blog/apply.html', {'posts': posts, 'form': form, 'jd': jd, 'resume': resume})

    return render(request, 'blog/apply.html', {'posts': posts, 'form': form})

# get personal info from the username




