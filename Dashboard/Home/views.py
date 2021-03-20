from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    context = {
        'key' : 'value',
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is About page")

def services(request):
    return HttpResponse("this is Services page")

def contact(request):
    return HttpResponse("this is Contact page")