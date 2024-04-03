from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10,'b':200,'c':100}

    return render(request,'condition.html',d)
def name(request):
    d={'name':'jasu'}
    return render(request,'name.html',d)

