from django.db import models
from django.urls import reverse
from customer.models import Customer

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])

class Product(models.Model):
    #FK 
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name_plural = 'products'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	complete = models.BooleanField(default=False)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	total_order = models.IntegerField(default=0, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address