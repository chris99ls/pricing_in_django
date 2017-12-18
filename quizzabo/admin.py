from django.contrib import admin
from .models import Pricing
from .models import Item
# Register your models here.

admin.site.register(Pricing)
admin.site.register(Item)