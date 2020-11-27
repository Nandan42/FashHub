from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Product(models.Model):
    mainimage = models.ImageField(blank=True)
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    img3 = models.ImageField(blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    studio_name = models.CharField(max_length=300,null=True)
    size = models.CharField(max_length=300,null=True)
    gender = models.CharField(max_length=300,null=True)
    category = models.CharField(max_length=300,null=True)
    rent_price = models.FloatField(null=True)
    count = models.IntegerField(default=0)

    rented = models.BooleanField(default=False)
    

    def __str__(self):
        return self.category


class events(models.Model):
    name = models.CharField(max_length=300,null=True)
    organizer_name = models.CharField(max_length=300,null=True)
    bio = models.TextField(max_length=1000,null=True)
    #image = models.IntegerField(blank=True)
    #link = models.CharField(max_length=300,null=True)
    phone_number = models.IntegerField(blank=True)
    email = models.CharField(max_length=300,null=True)
    venue = models.CharField(max_length=300,null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Journal(models.Model):
    img_front = models.ImageField(blank=True)
    img = models.ImageField(blank=True)
    category = models.CharField(max_length=300,null=True)
    title = models.CharField(max_length=300,null=True)
    date = models.DateField(null=True)
    author = models.CharField(max_length=300,null=True)
    details = models.TextField(max_length=1000,null=True)
    content = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300,null=True)
    details = models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.category

class Wishlist(models.Model):
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.category

class Donations(models.Model):
    Name = models.CharField(max_length=300,null=True)
    email = models.CharField(max_length=300,null=True)
    phone_number = models.CharField(max_length=300,null=True)
    address = models.CharField(max_length=300,null=True)
    clothes_number = models.CharField(max_length=300,null=True)