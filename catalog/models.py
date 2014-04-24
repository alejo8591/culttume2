# -*- encoding: utf-8 -*-
from django.db import models

# Category Models.
class Category(models.Model):
	name = models.CharField(max_length=50);
	""" 
		Slug is a newspaper term. A slug is a short label for something, 
	    containing only letters, numbers, underscores or hyphens. 
	    They’re generally used in URLs. 
	"""
	slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for Product page URL, created from name.')
	description = models.TextField(help_text='Description for Products')
	is_active = models.BooleanField(default=True)
	tag_keywords = models.CharField(max_length=255, help_text='Meta Keywords comma-delimited set of SEO Keywords')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at =  models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'categories'
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('catalog_category', (), {'category_slug' : self.slug})

# Product Models
class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length=255, unique=True, help_text='Meta Keywords comma-delimited set of SEO Keywords')
	brand = models.CharField(max_length=255)
	# Stock-keeping unit
	# sku = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
	old_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0.00)
	image = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_bestseller = models.BooleanField(default=False)
	quantity = models.IntegerField()
	description = models.TextField()
	tag_keywords = models.CharField(max_length=255, help_text='Meta Keywords comma-delimited set of SEO Keywords')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at =  models.DateTimeField(auto_now=True)
	categorie_product = models.ManyToManyField(Category)

	class Meta:
		db_table = 'products'
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('catalog_category', (), {'product_slug' : self.slug})

	def sale_price(self):
		if self.old_price > self.price:
			return self.price
		else: 
			return None

