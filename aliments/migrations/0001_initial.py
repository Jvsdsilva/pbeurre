# Generated by Django 2.2.6 on 2020-01-04 14:06

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategory', models.CharField(max_length=200)),
                ('nameCategory', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idStore', models.CharField(max_length=200)),
                ('nameStore', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAlim', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('descriptionAlim', models.CharField(blank=True, max_length=3000, null=True)),
                ('nutritionGrade', models.CharField(blank=True, max_length=200, null=True)),
                ('idCategory', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aliments.Category')),
                ('idStore', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aliments.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Foodsave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAliment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aliments.Products')),
                ('idUser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
