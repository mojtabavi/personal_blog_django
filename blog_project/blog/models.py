from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_convertor

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children',verbose_name='دسته والد' )
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته ها"
        ordering = ['parent_id','position']
    def __str__(self):
        return self.title

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="p")

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True,verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images",verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name="وضعیت")
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    #نمایش عکس های بند انگشتی در پنل ادمین
    def thumbnail_tag(self):
        return format_html("<img width=120 src='{}' style='border-radius: 5px;'>".format(self.thumbnail.url))
    thumbnail_tag.short_description ="عکس بند انگشتی"


    objects = ArticleManager()



class TitleSettings(models.Model):
    POSITION_CHOICES = (
        ('site', 'عنوان سایت'),
        ('navbar', 'لوگو منو اصلی'),
        ('copyright', 'کپی رایت'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    position = models.CharField(max_length=50, verbose_name="موقعیت در سایت", primary_key=True, choices=POSITION_CHOICES)

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.title