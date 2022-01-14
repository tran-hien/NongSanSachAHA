from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views import generic
from django.db.models import Count
from django.views.generic.list import ListView
from . import models
from product.models import Product,Category
from django.db.models import Q
from django.core.paginator import Paginator
import product
# Create your views here.
def search(request):
    """ search function  """
    if request.method=="POST":
        q = request.POST['q']
        multiple_q = Q(Q(title__icontains=q) | Q(price__icontains=q)|Q(description__icontains=q))
        data = Product.objects.filter(multiple_q)
    else:
        data = Product.objects.all()
    context = {
        'data': data
    }
    return render(request, 'product/search.html',
    context )
def freshfruit(request):

    fresh_products =Product.objects.all().filter(Q(category_id=2))
    p = Paginator(fresh_products, 3)
    page_number = request.GET.get('page',1)
    page_obj = p.page(page_number)
    context = {'product_item': page_obj}
    return render(request,'product/freshfruit.html',context )

def drinkfruit(request):
    drink_products = models.Product.objects.filter(Q(category_id=4))
    p = Paginator(drink_products, 3)
    page_number = request.GET.get('page',1)
    page_obj = p.page(page_number)
    context = {'product_item': page_obj}
    return render(request,'product/drinkfruit.html',context )

def driedfruit(request):
    dried_products =    Product.objects.filter(Q(category_id=3))
    p = Paginator(dried_products, 3)
    page_number = request.GET.get('page',1)
    page_obj = p.page(page_number)
    context = {'product_item': page_obj}
    return render(request,'product/driedfruit.html',context )

def vegetable(request):
    vegetable = models.Product.objects.filter(Q(category_id=1))
    p = Paginator(vegetable, 3)
    page_number = request.GET.get('page',1)
    page_obj = p.page(page_number)
    context = {'product_item': page_obj}
    return render(request,'product/vegetable.html',context )

class ProductClass(ListView):
    template_name = 'product/product.html'
    paginate_by=2
    model=Product
    context_object_name = 'page_obj'
    queryset = Product.objects.all()
    
    def get_context_data(self,**kwargs):
        all_products = Product.objects.all()
       # phan trang
        p = Paginator(all_products, 6)
        page_number = self.request.GET.get('page',1)
        page_obj = p.page(page_number)
    
        #sorting 
        product_order_price=''
        sorting = self.request.GET.get('sorting', '')
        if sorting != '':
            if sorting=='high-low':
                product_order_price=Product.objects.all().order_by('-price')
            if sorting=='low-high':
                product_order_price=Product.objects.all().order_by('price')
            if sorting=='title':
                product_order_price=Product.objects.all().order_by('title')    
        context=super(ProductClass,self).get_context_data(**kwargs)
       
        
        product_count=models.Product.objects.all().count()
        context = {'product_items': all_products, 'product_count': product_count,
         'product_item':product_order_price, 'sorting':sorting,
         'product_items': page_obj}
        return context
    

class ProductDetail(TemplateView):
    def get(self, request, product_id):
        product_detail_item = models.Product.objects.get(pk=product_id)
        return render(request, "product/product_details.html", {'pd': product_detail_item})

class CategoriesClass(TemplateView):
    template_name = 'product/product.html'
    
    def get(self, request):
        all_categories = Category.objects.all()
        context = {'categories': all_categories}
        return render(request, "homepage/hero_section.html", context)

class CategoriesList(generic.ListView):
    template_name = 'product/category_details.html'
    context_object_name = 'categories'
    queryset = models.Category.objects.all().annotate(num_products=Count('product'))
