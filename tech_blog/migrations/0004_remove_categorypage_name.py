# Generated by Django 3.2.11 on 2022-01-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech_blog', '0003_auto_20220120_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorypage',
            name='name',
        ),
    ]
