from django.shortcuts import render
from product.models import Item
def test_case1(request):
    Data=Item.objects.all()
    return render(request,"application/s1.html",{'Data':Data})
