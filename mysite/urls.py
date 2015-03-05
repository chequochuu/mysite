from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

def detail(request):    
    return HttpResponse("VNOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

urlpatterns = [
    url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', detail, name='detail'),
]
