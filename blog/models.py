from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_image")
    title = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, blank=True, unique=True)


    def __str__(self):
        return self.name


STATUS =(
    (0, 'Draft'),
    (1, 'Published'),
  
)
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(blank=True )
    content =models.TextField(null=True, blank=True)
    created_on = models.DateTimeField()
    cover = models.ImageField(null=True, blank=True )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url


class Comment(models.Model):
    commenter = models.CharField(max_length = 50)
    body = models.TextField()
    post = models.ForeignKey(Post, null=True, on_delete = models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body


class About(models.Model):
    text = models.TextField(null=True, blank=True)

    


class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    face_book = models.URLField(blank=True, null=True)
    linkedin =  models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    sof = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)


