# Generated by Django 3.2.22 on 2023-10-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic_category',
            field=models.CharField(choices=[('Recycling', 'Recycling'), ('Food', 'Food'), ('Clothing', 'Clothing'), ('Recipes', 'Recipes'), ('Energy', 'Energy'), ('Products', 'Products'), ('Transport', 'Transport')], default='Recycling', max_length=50),
        ),
    ]
