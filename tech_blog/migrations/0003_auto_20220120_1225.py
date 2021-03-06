# Generated by Django 3.2.11 on 2022-01-20 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('tech_blog', '0002_auto_20220119_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('name', models.CharField(max_length=200, verbose_name='Título categoría')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='articledetailpage',
            options={'verbose_name': 'Detalle Artículo', 'verbose_name_plural': 'Detalle Artículos'},
        ),
        migrations.AlterModelOptions(
            name='articlelistingpage',
            options={'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='category',
            field=models.ManyToManyField(blank=True, to='tech_blog.CategoryPage', verbose_name='Categoría'),
        ),
    ]
