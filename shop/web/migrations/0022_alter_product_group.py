# Generated by Django 4.1 on 2022-08-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('pc', 'pc'), ('notebook', 'notebook'), ('accessories', 'accessories'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]