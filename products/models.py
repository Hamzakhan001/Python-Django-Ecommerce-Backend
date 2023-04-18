from django.db import models
from base.models import BaseModel

# Create your models here.


class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload="categories")
    
    

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="products")
    price=models.IntegerField()
    description=models.TextField(max_length=200)
    

class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload="product")
    
    
    
    
    # class Meta:
        
