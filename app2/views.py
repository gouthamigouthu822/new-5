from django.shortcuts import render
def jinja_print1(request):
    d={'Name':'Aravind'}
    return render(request,'jinja_print1.html',context=d)
# Create your views here.

# Create your views here.
