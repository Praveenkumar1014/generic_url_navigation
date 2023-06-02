from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'manju'}
    return render(request,'wish.html',context=d)
def conditions(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',context=d)
def loop(request):
    s={'name':'praveen'}
    return render(request,'loop.html',s)
