from django.db import models

# Create your models here.

class Pricing(models.Model):
       
    PRICING_TYPE = (
        ('FREE', 'FREE'),
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('EXPERT', 'EXPERT'),
        
    )

    type = models.CharField(
        max_length=20,
        choices= PRICING_TYPE,
        default='FREE',
    )
    
    price = models.CharField(max_length=20)
       
    
    class Meta:
        verbose_name_plural='Prices'

    def __str__(self):
        return self.type

    


class Item(models.Model):
    
    description=models.CharField(max_length=30,blank=True,null=False)
    pricing=models.ForeignKey(Pricing)

    def __str__(self):
        return self.description + '(' + self.pricing.type + ')'
