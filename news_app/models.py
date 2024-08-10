from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE
                                 )
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
        )
    
    objects = models.Manager()
    from .managers import PublishedManager
    published = PublishedManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News,self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-published_at']

    def _str__(self) -> str:
        return f"{self.title}"

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name