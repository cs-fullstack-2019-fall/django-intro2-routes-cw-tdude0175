from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcome to index")

def gogetthegood(request):
    return HttpResponse("Here you go! Got this Video done!")

def happy(request):
    return HttpResponse("Ren & Stimpy rocks!")

def new(request,string):
    return HttpResponse(string)