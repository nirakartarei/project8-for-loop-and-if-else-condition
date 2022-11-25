from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':100,'b':300}
    return render(request,'a1_first.html',d)
def a1_second(request):
    d={'a':400,'b':600,'c':800}
    return render(request,'a1_second.html',d)
