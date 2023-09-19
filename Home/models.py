from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy

# Create your models here.
class catagory (models.Model):
    c_name = models.CharField(max_length=100,unique=True)
    c_image = models.ImageField(upload_to='ctgry_Image')
    c_slug = models.SlugField(max_length=100,unique=True)
    
    class Meta:
        ordering =('c_name',)
        verbose_name='catagory'
        verbose_name_plural='catagories'

    def __str__(self):
        return self.c_name.upper()
    
    def get_url(self):
        # return reverse('prod_cat',args=[self.c_slug])
        return reverse('Home:prod_cat',args=[self.c_slug])

class products (models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_image = models.ImageField(upload_to='Pdt_Image') 
    p_desc = models.TextField()   
    p_stock = models.IntegerField()
    p_available = models.BooleanField()
    p_slug = models.SlugField(max_length=100,unique=True)
    catagory = models.ForeignKey(catagory,on_delete=models.CASCADE)
    
    def desc(self,obj):
        if len(obj.p_desc)>15:
            return obj.p_desc[:15]+'...'
        else:
            return obj.p_desc
            
    desc.short_description = 'p_description' 

    def __str__(self):
        return '{}'.format(self.p_name.upper())
     
    def get_url(self):
        # return reverse('prod_cat',args=[self.c_slug]) 
        return reverse('Home:item', args=[self.pk])
