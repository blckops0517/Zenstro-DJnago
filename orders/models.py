from django.db import models
from accounts.models import Account
from store.models import Product,Variation

# Create your models here.
# FOR PLACE ORDER --- METHODS  
class Payment(models.Model):
    user            =   models.ForeignKey(Account,on_delete=models.CASCADE)
    payment_id      =   models.CharField(max_length=100)
    payment_method  =   models.CharField(max_length=100)    # WE HAVE ONLY PAYPAL
    amount_paid     =   models.CharField(max_length=100)    # THIS IS TOTAL AMOUNT PAID 
    status          =   models.CharField(max_length=100)
    created_at      =   models.DateTimeField(auto_now_add=False)
     
    def __str__(self):
        return self.payment_id
    
# ORDER METHOD 

class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    
    user            =   models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    payment         =   models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number    =   models.CharField(max_length=50)
    first_name      =   models.CharField(max_length=100)
    last_name       =   models.CharField(max_length=100)
    phone           =   models.CharField(max_length=100)
    email           =   models.EmailField(max_length=254)
    address_line_1  =   models.CharField(max_length=200)
    address_line_2  =   models.CharField(max_length=200,blank=True)
    country         =   models.CharField(max_length=100)       
    state           =   models.CharField(max_length=100)       
    city            =   models.CharField(max_length=100)    
    order_note      =   models.CharField(max_length=100,blank=True)
    order_total     =   models.FloatField()
    tax             =   models.FloatField()
    status          =   models.CharField(max_length=50,choices=STATUS,default="New")
    ip              =   models.CharField(max_length=50,blank=True)
    is_ordered      =   models.BooleanField(default=False)
    created_at      =   models.DateTimeField(auto_now_add=True)   
    updated_at      =   models.DateTimeField(auto_now=True)   
    
    # ACCESS FULL NAME
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
     # ACCESS FULL ADDRESS
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
    
    def __str__(self):
        return self.first_name
    
# FINAL MODEL FOR ORDER PRODUCT 

class OrderProduct(models.Model):
    order        =  models.ForeignKey(Order,on_delete=models.CASCADE)  
    payment      =  models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)   
    user         =  models.ForeignKey(Account,on_delete=models.CASCADE)
    product      =  models.ForeignKey(Product,on_delete=models.CASCADE)
    variation    =  models.ForeignKey(Variation,on_delete=models.CASCADE) 
    color        =  models.CharField(max_length=50)
    size         =  models.CharField(max_length=50)
    quantity     =  models.IntegerField()
    product_price=  models.FloatField()
    ordered      =  models.BooleanField(default=False)
    created_at   =  models.DateTimeField(auto_now_add=True)
    updated_at   =  models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.product_name
    
    
