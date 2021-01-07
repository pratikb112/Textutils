# I have created this website- pratik

#def index(request):
    #return HttpResponse ("<h1>Navigation Bar</h1> <h2>Proffessional  Profile <a href='https://www.linkedin.com/in/pratik-balladkar-61a31a158/'>My linkedin profile</a></h2><br><h2>Social Media Platform <a href='https://www.facebook.com/pratik.balladkar'>My facebook profile</a>")

#def about(request):
    #return HttpResponse ("about Pratik")

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext= request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)
    print(removepunc)
    #if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char

    params={'purpose':'remove punctuations','analyzed_text': analyzed}
    return render(request,'analyze.html',params)
    #else:
        #return HttpResponse("Error")

#def capfirst(request):
    #return HttpResponse("capefirst")
#def newlineremove(request):
    #return HttpResponse("new line remove")
#def spaceremover(request):
    #return HttpResponse("remove space")
#def charcounter(request):
    #return HttpResponse("charcount")