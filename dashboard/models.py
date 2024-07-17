from django.db import models
from django.utils import timezone

# Create your models here.
CATEGORY = [
      ('desktops', 'desktops'),
      ('laptops', 'laptops'),
      ('extensions', 'extensions'),
      ('screens', 'screens'),
      ('banners', 'banners'),
]

class New_Asset(models.Model):
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity =models.PositiveIntegerField (null=True)
    approved_at = models.DateTimeField(null=True, blank=True)  

    def approve(self):
        self.approved_at = timezone.now()
        self.save()

    def __str__(self):
            return f'{self.category} : {self.quantity}'


class Asset(models.Model):
    category = models.CharField(max_length=100,choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    borrowing_time = models.DateTimeField(null=True, blank=True)
    returning_time = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    def approve(self):
        self.approved_at = timezone.now()
        self.save()

    def __str__(self):
          return f'{self.category} : {self.quantity}'
    
class Maintainance(models.Model):
      category = models.CharField(max_length=100,choices=CATEGORY, null=True)
      quantity = models.PositiveIntegerField(null=True)
      comment = models.TextField(null=True, blank=True)
      def __str__(self):
           return f'{self.category} : {self.quantity}'