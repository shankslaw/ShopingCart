from django.contrib import admin
from . models import *
# Register your models here.

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'c_slug':('c_name',)}
    list_display = ['c_name']
admin.site.register(catagory,CatAdmin)

class PdtAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'p_slug' : ('p_name',)}
    list_display = ['p_name','p_price','p_stock','p_desc','p_image','p_stock','p_available']
    list_editable = ['p_price','p_stock','p_desc','p_image','p_stock','p_available']
admin.site.register(products,PdtAdmin)