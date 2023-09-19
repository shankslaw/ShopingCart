from django.shortcuts import render,redirect,get_object_or_404
from Home.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(req,tot=0,count=0,ct_items=None):
    try:
        ct = CartList.objects.get(cart_id = c_id (req))
        ct_items = Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prdt.p_price*i.qnty)
            count += i.qnty
    except ObjectDoesNotExist:
        pass    
    return render(req,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

#creating session id for cart per user
def c_id(req):
    ct_id = req.session.session_key
    if not ct_id:
        ct_id = req.session.create()
    return ct_id 

#for items to the cart
def add_cart (req,product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(req))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(req))
        ct.save()
    try:
        c_items = Items.objects.get(prdt=prod,cart=ct)
        if c_items.qnty < c_items.prdt.p_stock:
            c_items.qnty +=1
        c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(prdt=prod,qnty=1,cart=ct)
        c_items.save()
    return redirect('cart_details')

def min_cart(req,product_id):
    ct = CartList.objects.get(cart_id=c_id(req))
    prod = get_object_or_404(products,id=product_id)
    c_items = Items.objects.get(prdt=prod,cart=ct)
    if c_items.qnty>1:
        c_items.qnty-=1
        c_items.save()
    else:
        c_items.delete()    
    return redirect('cart_details')    

def cart_delete(req,product_id):
    ct = CartList.objects.get(cart_id=c_id(req))
    prod = get_object_or_404(products,id=product_id)
    c_items = Items.objects.get(prdt=prod,cart=ct)
    c_items.delete()
    return redirect('cart_details')



                                
