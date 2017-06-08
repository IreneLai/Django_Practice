from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from mysite.settings import MEDIA_URL
from diary.models import Map,Diary,Tag,Media,DiaryForm,MediaForm
from decimal import *
from django.core import serializers
# Create your views here.

def map(request):
    if request.method == 'POST':
        getlat = Decimal(request.POST.get('lat'))
        getlon =  Decimal(request.POST.get('lon'))
        getloc = request.POST.get('loc')
        newloc = Map.objects.create(location=getloc, latitude=getlat, longitude=getlon)
        newloc.save()
        return HttpResponseRedirect('/mapdisplay/')
    return render(request,'map.html')

def mapdisplay(request):
    import json
    maps = Map.objects.all()
    data = serializers.serialize("json", maps)
    maplist = list(maps)
    test = maps[0].location
    return render(request,'mapdisplay.html',locals())

def diary_edit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DiaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_diary = form.save(commit=False)
            new_diary.save()
            return HttpResponseRedirect('/diary/')
        else:
            raise Http404
    else:
        form = DiaryForm()
    return render(request, 'diary-edit.html', locals())

def diary(request):
    diarys = Diary.objects.all()
    medias = Media.objects.all().delete()
    return render(request, 'diary.html', locals())

def uploadImg(request):
    if request.method =='POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/img/')
        else:
            raise Http404
    else:
        form = MediaForm()
    return  render(request,'uploadImg.html',locals())

def showMedia(request):
    if request.method == 'POST':
        deleteID=request.POST.get('dID')
        Media.objects.get(id=deleteID).delete()
        return HttpResponseRedirect('/media/')
    imgs= Media.objects.all()
    mediaurl = MEDIA_URL
    return render(request,'showmedia.html',locals())

def demo(request):
    return render(request,'demo.html')