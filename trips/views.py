from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#import from model
from .models import Post
from .models import Category
from django.shortcuts import render_to_response


def hello_world(request):
    return render(request,'hello_world.html',{
    	'current_time': str(datetime.now()),
    	})
    #render：產生 HttpResponse 物件

def home(request):
	post_list = Post.objects.all()
	return render(request,'home.html',{
		'current_time': datetime.now(),
		'post_list':post_list,
		})

def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	return render(request,'post.html',{'post':post})

def test_db(request):
	food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
	food2 = { 'name':'番茄', 'price':60, 'comment':'好吃', 'is_spicy':True }
	foods = [food1,food2]
	return render(request,'test.html',locals())