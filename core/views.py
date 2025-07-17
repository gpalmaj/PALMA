from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def drumkits(request):
    return render(request, "drumkits.html")

def samples(request):
    return render(request, "samples.html")

def plugins(request):
    return render(request, "plugins.html")
