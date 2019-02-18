from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=15
    )
    article = models.CharField(
        max_length=6
    )
    country = models.CharField(
        max_length=15
    )
    pakaging = models.CharField(
        max_length=30
    )
    figure = models.CharField(
        max_length=15
    )

    image = models.ImageField(
        upload_to='',
        blank=True
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"



class Description(models.Model):
    article = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    material = models.CharField(
        max_length=15
    )

    size = models.FloatField()

    dimension = models.CharField(
        max_length=2
    )

    def __str__(self):
        return f"{self.article.name}"

class Package(models.Model):
    width = models.FloatField()
    heigth = models.FloatField()
    length = models.FloatField()
    volume = models.FloatField()
    article = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.article.name}"
