from django.db import models
from django.urls import  reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Posts(models.Model):
    users=models.ForeignKey('auth.User', verbose_name='yazar', on_delete=models.PROTECT, related_name="posts")
    title=models.CharField(max_length=120 , verbose_name="Başlık")
    content=RichTextField(verbose_name="İçerik")
    publishDate=models.DateField(verbose_name="Yayınlanma Tarihi" , auto_now_add=True)
    image=models.ImageField(null=True, blank=True,verbose_name="Resim 900*500")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_post_app_name:detay',kwargs={'pk':self.id})

    
    def get_post_create(self):
        return reverse('blog_post_app_name:postCreated')

    

    def get_post_update(self):
        return reverse('blog_post_app_name:guncelle',kwargs={'pk':self.id})


    def get_post_delete(self):
        return reverse('blog_post_app_name:silme',kwargs={'pk':self.id})


  
    class Meta:
        ordering=['-publishDate' , '-id']

    

class comment(models.Model):
    postComment=models.ForeignKey('Posts' ,verbose_name="Post" , related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="isim")
    content=models.TextField(verbose_name="Yorum")

    created_date=models.DateField(auto_now_add=True)

    # return "/post/{}".format(self.id)