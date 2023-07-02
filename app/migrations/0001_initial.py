# Generated by Django 4.2.2 on 2023-07-02 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('image1', models.ImageField(upload_to='product/image1/')),
                ('image2', models.ImageField(upload_to='product/image2/')),
                ('image3', models.ImageField(upload_to='product/image3/')),
                ('image4', models.ImageField(upload_to='product/image4/')),
                ('price', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
