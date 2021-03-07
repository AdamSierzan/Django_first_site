from django.shortcuts import render
from .models import Post


# Create your views here.
# we create a function is going to handle the traffic from the home page of our blog
# it takes request arg and returns what a user will see




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)


# we havent met our url patter to this view func yet so we have to do it now


# now let's make a new route to about site
def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
