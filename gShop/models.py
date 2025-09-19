from django.db import models
from django.contrib.auth.models import User

class Gold(models.Model):
  weight = models.IntegerField()
  picture = models.ImageField()
  
class Wishlist(models.Model):
  customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  wished_item = models.ForeignKey(Gold, on_delete=models.CASCADE)
  slug = models.CharField(max_length=30, null=True, blank=True)

  def __str__(self):
      return f"{self.customer.username} - {self.wished_item}"
  
  