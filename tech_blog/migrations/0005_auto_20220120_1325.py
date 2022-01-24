# Generated by Django 3.2.11 on 2022-01-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tech_blog', '0004_remove_categorypage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articledetailpage',
            name='category',
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tech_blog.categorypage', verbose_name='Categoría'),
        ),
    ]
