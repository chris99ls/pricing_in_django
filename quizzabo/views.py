from django.shortcuts import render
from . models import Pricing

# Create your views here.

def price_list(request):
	all_pricing=Pricing.objects.all()
	return render(request,'quizzabo/price_list.html',{'all_pricing': all_pricing})