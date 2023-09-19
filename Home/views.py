from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(req,slug=None):
    c_page=None
    pdts=None
    if slug!=None:
        # here catagory is model
        c_page=get_object_or_404(catagory,c_slug=slug)
        # here catagory is foreign key of model product
        pdts = products.objects.filter(catagory=c_page,p_available=True)
    else:
        pdts = products.objects.all().filter(p_available=True)
    ct = catagory.objects.filter    
    paginator = Paginator(pdts,2)
    try:
        page = int(req.GET.get('page','1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)    
    except (EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(req,'index.html',{'products':pdts,'ctgry' : ct, 'pg': pro})


def root(req):
    return render(req,'root.html')

def item(req,pk):
    id=products.objects.get(id=pk)
    return render(req,'view_item.html',{'ids': id})  

def search(req):
    prod=None
    query=None
    if 'q' in req.GET:
        query=req.GET.get('q')
        prod=products.objects.all().filter(Q(p_name__contains=query)|Q(p_desc__contains=query))

    return render(req,'search.html',{ 'qr':query,'pr': prod})
     
  