from django.db import models
from django.utils import timezone
# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','Masala Latte'),
        ('GL','Ginger Latte'),
        ('CL','Cardamom Latte'),
        ('HL','Honey Latte'),
        ('TL','Turmeric Latte'),
    ]
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
  

    def __str__(self):
        return self.name