# Generated by Django 3.0.5 on 2020-04-13 14:29
# Migración manual para agregar un registro en la tabla Category,
# que será usado como categoría predeterminada para los post
# registrados en BD

from django.db import migrations
# from blog.models import Category # no es posible

def insert_default_category(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    Category.objects.create(name='Default Category', description='Default category')

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200413_0927'),
    ]

    operations = [
        migrations.RunPython(insert_default_category)
    ]