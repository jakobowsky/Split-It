from django.db import models
from django.utils import timezone
from PIL import Image


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='brand_pics')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Brand, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='promotions',
    )
    price = models.FloatField()
    image = models.ImageField(default='default.jpg',
                              upload_to='promotion_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Promotion, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
