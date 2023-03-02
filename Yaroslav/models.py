from django.db import models





class Basket(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    products = models.ManyToManyField('Product', blank=True, through='BasketProduct', related_name='basket1')

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.TextField()
    basket = models.ManyToManyField(Basket, blank=True, through='BasketProduct', related_name='products1')


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
