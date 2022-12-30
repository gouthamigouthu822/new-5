from django.shortcuts import render
def jinja_print(request):
    d={'Name':'Gouthami'}
    return render(request,'jinja_print.html',context=d)
# Create your views here.
