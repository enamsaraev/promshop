# Generated by Django 4.2.4 on 2023-09-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0011_alter_sliderchildinfo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderchildinfo',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]
