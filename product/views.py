from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
# Create your views here.


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
