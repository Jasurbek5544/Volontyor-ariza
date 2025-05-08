from django.db import models

# Create your models here.

class Viloyat(models.Model):
    nomi = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"

class Tuman(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name='tumanlar')
    nomi = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"

class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    yashash_joyi = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    passport_image = models.ImageField(upload_to='passports/')
    selfi_image = models.ImageField(upload_to='selfies/')
    status = models.CharField(max_length=20, choices=[
        ('new', 'Yangi'),
        ('in_progress', 'Ko\'rib chiqilmoqda'),
        ('accepted', 'Qabul qilingan'),
        ('rejected', 'Bekor qilingan')
    ], default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def manzil(self):
        return f"{self.viloyat.nomi}, {self.tuman.nomi}, {self.yashash_joyi}"
    
    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"
