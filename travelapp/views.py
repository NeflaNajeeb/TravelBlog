from django.http import HttpResponse
from django.shortcuts import render
from .models import tb_Place, tb_teammem


# Create your view
# s here.
def demo(request):
    obj=tb_Place.objects.all()
    obj1=tb_teammem.objects.all()
    return render(request,'index.html',{'result':obj,'team':obj1})