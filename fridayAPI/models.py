from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ShoppingListItems(models.Model):
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)
    approx_cost = models.FloatField(blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name