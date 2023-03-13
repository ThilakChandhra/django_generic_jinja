from django.shortcuts import render

# Create your views here.
def generic(request):
    d={'name':'Thilak','age':23}
    return render(request,'first.html',context=d)