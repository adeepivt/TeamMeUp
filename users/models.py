from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    img = models.ImageField(default='e_logo.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.img.path)
        if image.height>300 and image.width>300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.img.path)