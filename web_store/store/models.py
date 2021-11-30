from django.db import models


# Create your models here.
from django.db.models import UniqueConstraint
from django.urls import reverse


class Product(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    image = models.ImageField('Изображение', upload_to='cases/%Y/%m/%d')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_page', kwargs={'product_slug': self.slug})


class Category(models.Model):
    name = models.CharField('Наименование категории', max_length=200, db_index=True)
    slug = models.SlugField('URL', max_length=200, db_index=True, unique=True, null=True)
    image = models.ImageField('Изображение', upload_to='category/%Y/%m/%d', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.CharField(max_length=30, db_index=True, verbose_name='Брэнд')
    model = models.CharField(max_length=30, db_index=True, verbose_name='Модель')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL', unique=True)

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
        #UniqueConstraint(fields=['product_id', 'phone_id'], name='id_product_to_phone')
        unique_together = (('product_id', 'phone_id'), )

        ordering = ('product_id',)
        verbose_name = 'Продукт-Телефон'
        verbose_name_plural = 'Продукты-Телефоны'

class Property(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование свойства')
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='ID продукта', default=1)
    value = models.CharField(max_length=100, db_index=True, verbose_name='Значение', null=True)
    unit = models.CharField(max_length=20, verbose_name='Ед. измерения', null=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'

    def __str__(self):
        return self.name


# class Value(models.Model):
#     property_id = models.ForeignKey('Property', on_delete=models.PROTECT, verbose_name='ID свойства')
#     weight = models.CharField(max_length=200, db_index=True, verbose_name='Вес значения')
#
#     class Meta:
#         ordering = ('property_id',)
#         verbose_name = 'Значение свойства'
#         verbose_name_plural = 'Значения свойств'


# class PropertyToProduct(models.Model):
#     product_id = models.ForeignKey('Product', on_delete=models.PROTECT, primary_key=True, verbose_name='ID товара')
#     property_id = models.ForeignKey('Property', on_delete=models.PROTECT, verbose_name='ID свойства')
#
#     class Meta:
#         UniqueConstraint(fields=['product_id', 'property_id'], name='id_property_to_product')
#         # unique_together = (('key1', 'key2'),) - устаревший вариант
#
#         ordering = ('product_id',)
#         verbose_name = 'Свойство-Продукт'
#         verbose_name_plural = 'Свойства-Продукты'


class Storage(models.Model):
    product_id = models.ForeignKey('Product', unique=True, on_delete=models.PROTECT, verbose_name='ID товара')
    quantity = models.PositiveIntegerField('Количество')

    class Meta:
        ordering = ('product_id',)
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'

    def __str__(self):
        return self.quantity


class Customer(models.Model):
    first_name = models.CharField(max_length=30, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, db_index=True, verbose_name='Фамилия')
    phone_number = models.TextField(max_length=10, unique=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Эл. почта')

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.last_name


'''
Не удалять!
'''


# class Cart(models.Model):
#     #customer_id = models.ForeignKey('Customer', on_delete=models.PROTECT, unique=True, verbose_name='ID покупателя', default=1)
#     product_id = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='ID товара')
#     quantity = models.PositiveIntegerField('Количество', null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена', null=True)
#
#
#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Корзина'
#         verbose_name_plural = 'Корзины'




#
# class ProductToCart(models.Model):
#     cart_id = models.ForeignKey('Cart', primary_key=True, on_delete=models.PROTECT, verbose_name='ID корзины')
#     product_id = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='ID товара')
#     quantity = models.PositiveIntegerField('Количество', null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена', null=True)
#
#
#     class Meta:
#         UniqueConstraint(fields=['cart_id', 'product_id'], name='id_product_to_cart')
#         ordering = ('cart_id',)
#         verbose_name = 'Корзина-продукт'
#         verbose_name_plural = 'Корзины-продукты'
#
