from django.urls import path,include
from . import views

app_name='Home'

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:slug>',views.index,name='prod_cat'),
    path('item/<int:pk>',views.item,name='item'),
    path('search/',views.search,name='search'),
    path('root/',views.root,name='root'),
]

