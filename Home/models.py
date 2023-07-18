from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField( User, verbose_name=("User"), on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(("Name"), max_length=200,null=True)
    email=models.CharField(("Email"), max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(("Name"), max_length=200,null=True)
    price=models.FloatField(("Price"))
    digital=models.BooleanField(("Digital"),default=False,null=True,blank=False)
    image=models.ImageField(("Image"),null=True,blank=True, upload_to='products', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
         try:
              url=self.image.url
         except:
              url=''
         return url

class Order(models.Model):
    customer=models.ForeignKey(Customer, verbose_name=("Customer"), on_delete=models.SET_NULL,null=True,blank=True)
    date_orderd=models.DateTimeField(("Date Ordered"),auto_now_add=True)
    complete=models.BooleanField(("Complete"),default=False,null=True,blank=False)
    transaction_id=models.CharField(("Transaction id"), max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order, verbose_name=("Order"), on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
	



