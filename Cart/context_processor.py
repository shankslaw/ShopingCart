from . models import *
from . views import *

def count(req):
    itm_count=0;
    if 'admin' in req.path:
        return{}
    else:
        try:
            ct=CartList.objects.filter(cart_id=c_id(req))
            ctit=Items.objects.filter(cart=ct[:1])
            for i in ctit:
                itm_count += i.qnty

        except CartList.DoesNotExist:
            itm_count = 0
        return dict(itc = itm_count)        
