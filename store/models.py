from django.db import models

class Product(models.Model):

    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return sum(item.total_amount() for item in self.items.all())
    
class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def total_amount(self):
        return self.product.price * self.quantity
