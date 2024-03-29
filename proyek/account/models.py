from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)

class DataBlog(models.Model):
    judul = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='artikel/')
    teks = models.TextField()
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    # kategori = models.CharField(max_length=50)

    class Meta:
        ordering =['-id']

    def __str__(self):
        return self.judul