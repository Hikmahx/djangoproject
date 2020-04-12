from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("HELLO WORLD FROM POSTS")
    #for rendering template
    return render(request, 'posts/index.html', {'title': "Latest Posts"})