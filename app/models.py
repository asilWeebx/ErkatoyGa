from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=155)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="product/image1/")
    image2 = models.ImageField(upload_to="product/image2/")
    image3 = models.ImageField(upload_to="product/image3/")
    image4 = models.ImageField(upload_to="product/image4/")
    price = models.CharField(max_length=155)
    description = models.TextField()
    count = models.IntegerField()
    favourites = models.ManyToManyField(to='auth.User', related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.title
