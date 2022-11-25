from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':3000,'b':800,'c':900}
    return render(request,'a2_first.html',d)



def a2_second(request):
    d={'name':'nirakar'}
    return render(request,'a2_second.html',d)