from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

from .models import Product

class ProductDetailView(DetailView):
	model = Product
	#template_name = "product.html"



def product_detail_view_func(request,id):
	
	product_instance = get_object_or_404(Product,id=id)
	try:
		product_instance = get_object_or_404(id=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404
	product_instance = Product.objects.get(id=id)
	template = "products/product_detail.html"
	context = {
	"object":product_instance
	}
	return render(request,template,context) 