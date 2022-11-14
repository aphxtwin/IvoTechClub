from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import Categories, Posts

from .forms import contactForm
# Create your views here.



def home(request):
    submitted = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home/home.html', {'form': form, 'submitted':submitted,})

def writer_preview(request):
    post_list = Posts.objects.all()
    categories = Categories.objects.all()
    
    count = 0

    top_story = []
    secondary_stories = []
    other_stories = []

    for i in post_list:
        if i == post_list[len(post_list)-1]:
            top_story.append(i)
        elif i in post_list[len(post_list)-4:len(post_list)-1]:
            count = count + 1
            secondary_stories.append(i)
        else:
            other_stories.append(i)
    submitted = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form, 
        'submitted':submitted, 
        'top_story': top_story,
        'secondary_stories':secondary_stories,
        'count': count,
        'other_stories':other_stories,
        'categories': categories,
    }
    
    return render(request, 'home/the-writer.html', context )

def post_detailed(request, slug):
    detailed_post = Posts.objects.filter(slug = slug)

    context = {
        'slug': slug,
        'detailed_post': detailed_post,

    }
    return render(request, 'home/post.html', context)

def about(request):
    submitted = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'home/about.html', {'form': form, 'submitted':submitted})

def inventions(request):
    return render(request, 'home/inventions.html')