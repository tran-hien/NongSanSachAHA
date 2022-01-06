from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from .models import Product
from django.db.models import Q
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
    return render(request,'product/freshfruit.html',{} )

class ProductClass(TemplateView):
    template_name = 'product/product.html'

    def get(self, request):
        all_products = models.Product.objects.all()
        context = {'product_item': all_products}
        return render(request, "product/product.html", context)

class ProductDetail(TemplateView):
    def get(self, request, product_id):
        product_detail_item = models.Product.objects.get(pk=product_id)
        return render(request, "product/product_details.html", {'pd': product_detail_item})

class CategoriesClass(TemplateView):
    template_name = 'homepage/hero_section.html'
    
    def get(self, request):
        all_categories = models.Category.objects.all()
        context = {'categories': all_categories}
        return render(request, "homepage/hero_section.html", context)

    


