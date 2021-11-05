from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint
from django.urls import reverse


class Product(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    # extra_info_id = models.PositiveIntegerField()
    name = models.CharField('Наименование товара', max_length=100, db_index=True)
    slug = models.SlugField('URL', max_length=200, db_index=True, unique=True)
    image = models.ImageField('Изображение', upload_to='cases/%Y/%m/%d')
    description = models.TextField('Описание товара', blank=True)
    # phone_model_id = models.PositiveSmallIntegerField()
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('case_page', kwargs={'case_id': self.pk})


class Category(models.Model):
    name = models.CharField('Наименование категории', max_length=200, db_index=True)
    slug = models.SlugField('URL', max_length=200, db_index=True, unique=True)
    image = models.ImageField('Изображение', upload_to='category/%Y/%m/%d', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.CharField('Брэнд', max_length=30, db_index=True)
    model = models.CharField('Брэнд', max_length=30, db_index=True)

    class Meta:
        ordering = ('model',)
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.model


class ProductToPhone(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT, primary_key=True, verbose_name='ID категории')
    phone_id = models.ForeignKey('Phone', on_delete=models.PROTECT, verbose_name='ID телефона')

    class Meta:
        UniqueConstraint(fields=['product_id', 'phone_id'], name='id_product_to_phone')
        # unique_together = (('key1', 'key2'),) - устаревший вариант

        ordering = ('product_id',)
        verbose_name = 'Продукт-Телефон'

# class PostModel(models.Model):
#     author = models.CharField('Автор статьи', max_length=30)
#     title = models.CharField('Название статьи', max_length=50)
#     slug = models.SlugField('URL', max_length=60, unique=True, db_index=True, null=True, blank=True)
#     text = models.TextField('Текст статьи')
#     image = models.ImageField('Картинка к посту', upload_to='img')  # pillow
#     publish_date = models.DateTimeField('Время публикации', auto_now=True)
#     is_published = models.BooleanField('Пост опубликован?', default=True)
#     category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
