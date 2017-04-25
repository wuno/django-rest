from django.db import models

class Product(models.Model):
	product_id = models.CharField(max_length=255)
	product_name = models.CharField(max_length=255)
	product_url = models.CharField(max_length=255)
	advertiser = models.CharField(max_length=255)
	designer = models.CharField(max_length=255)
	image_url = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	commission = models.CharField(max_length=255)

	def __str__(self):
		return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.product_id, self.product_name, self.product_url, self.advertiser, self.designer, self.image_url, self.price, self.commission)
