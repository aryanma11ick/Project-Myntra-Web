from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#creating the first landing page
def index(request):
    code= """
    <h1>hello</h1>
    """
    #return HttpResponse(code)

    #returning the html page for the app
    html_page= "app/index.html"
    return render(request, html_app)


def index(request):
    #redirect("home")
    return HttpResponse("hello world")
