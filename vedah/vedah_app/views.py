from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hello(request):
    return HttpResponse("<h1>from hello</h1>")
    #return render(request, "vedah_app/templates/hello.html")
def index(request):
    student = "Ken Nduati"
    student_age = 4
    template = loader.get_template('vedah_app/hello.html')
    context =  {
        'student':student,
        'student_age': student_age,
    }
    return HttpResponse(template.render(context,request))

    #return HttpResponse("<p>paragraph</p>")
def products(request):
    template = loader.get_template('vedah_app/products.html')
    return HttpResponse(template.render())
