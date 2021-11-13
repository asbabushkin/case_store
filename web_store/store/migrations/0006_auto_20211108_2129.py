# Generated by Django 3.2.8 on 2021-11-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211102_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, max_length=30, verbose_name='Фамилия')),
                ('phone_number', models.TextField(max_length=10, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование свойства')),
            ],
            options={
                'verbose_name': 'Свойство',
                'verbose_name_plural': 'Свойства',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='phone',
            name='model',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Модель'),
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(db_index=True, max_length=200, verbose_name='Вес значения')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.property', verbose_name='ID свойства')),
            ],
            options={
                'verbose_name': 'Значение',
                'verbose_name_plural': 'Значения',
                'ordering': ('property_id',),
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.product', unique=True, verbose_name='ID товара')),
            ],
            options={
                'verbose_name': 'Остаток',
                'verbose_name_plural': 'Остатки',
                'ordering': ('product_id',),
            },
        ),
        migrations.CreateModel(
            name='PropertyToProduct',
            fields=[
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='store.product', verbose_name='ID товара')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.property', verbose_name='ID свойства')),
            ],
            options={
                'verbose_name': 'Свойство-Продукт',
                'ordering': ('product_id',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.customer', unique=True, verbose_name='ID покупателя')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProductToCart',
            fields=[
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='store.cart', verbose_name='ID корзины')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.product', verbose_name='ID товара')),
            ],
            options={
                'verbose_name': 'Корзина-продукт',
                'ordering': ('cart_id',),
            },
        ),
    ]
