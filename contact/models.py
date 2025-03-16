from django.db import models
from storefront.models import StoreGoods  # Import your product model


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    store_good = models.ForeignKey(
        StoreGoods, on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        store_good_title = self.store_good.name if self.store_good else "General Inquiry"
        return f"Request from {self.name} for {store_good_title}"

