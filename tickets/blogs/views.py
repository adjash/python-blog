from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import BlogPost
def index(request):
    latest_blog_list = BlogPost.objects.order_by('-pub_date')[:5]
    return HttpResponse("hellow, world, this is the index of our blogs app")

def blogPost(request):
    return HttpResponse("test blog-post response")