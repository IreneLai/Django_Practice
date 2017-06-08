"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#import view function from trips app
from trips.views import hello_world,home,post_detail,test_db
from restaurants.views import menu
from diary.views import map,diary_edit,diary,uploadImg,showMedia,demo,mapdisplay


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^$',home),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^test/$',test_db),
    url(r'^menu/$', menu),
    url(r'^map/$', map),
    url(r'^mapdisplay/$', mapdisplay),
    url(r'^diary-edit/$', diary_edit),
    url(r'^diary/$', diary),
    url(r'^img/$',uploadImg),
    url(r'^media/$',showMedia),
    url(r'^demo/$',demo)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)