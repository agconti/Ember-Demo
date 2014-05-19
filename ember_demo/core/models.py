from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    description = models.CharField(max_length=100)
    isOnSale = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to='product_image')

    def __unicode__(self):
        return "Product: %s" % (self.title)


class Review(TimeStampedModel):

    text = models.CharField(max_length=100)
    product = models.ForeignKey(related_name='reviews')

    def __unicode__(self):
        return "Review of %s" % (self.product.title)
