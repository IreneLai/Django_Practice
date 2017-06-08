from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from restaurants.models import Restaurant,Food
# Create your views here.
def menu(request):
	path = request.get_host()
	restaurants = Restaurant.objects.all()
	return render(request,'menu.html',locals())