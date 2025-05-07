from django.db import models

# Create your models here.

class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ko‘rib chiqilmoqda'),
        ('accepted', 'Qabul qilingan'),
        ('rejected', 'Bekor qilingan'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    passport_image = models.ImageField(upload_to='passports/')
    selfie_image = models.ImageField(upload_to='selfies/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
