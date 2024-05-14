from django.shortcuts import render

from tours.models import Cities
# Create your views here.
def tours(request):
    return render(request, 'tours/tours.html',{'data':enumerate(Cities.objects.all()) })

def showcity(request):
    return render(request,'tours/showcity.html')


def destinations(request):
    return render(request,'tours/noFavFound.html',{'msg':'destination cities'}) 



def visited(request):
    return render(request,'tours/noFavFound.html',{'msg':'visited cities'})


