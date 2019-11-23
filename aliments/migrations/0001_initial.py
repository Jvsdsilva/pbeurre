# Generated by Django 2.2.5 on 2019-09-29 14:42
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=200, unique=True)),
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
                ('nameAlim', models.CharField(max_length=200, unique=True)),
                ('image', models.CharField(max_length=200, unique=True, blank=True, null=True)),
                ('url', models.CharField(max_length=500, unique=True, blank=True, null=True)),
                ('descriptionAlim', models.CharField(max_length=1500, unique=True, blank=True, null=True)),
                ('nutritionGrade', models.CharField(max_length=200, unique=True, blank=True, null=True)),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aliments.Category')),
                ('idStore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aliments.Store')),
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
