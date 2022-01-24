#Article listing and Article detail Page
from email.policy import default
from tabnanny import verbose
from django import forms
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField

# # Creating the listing articles page
# class ArticleListingPage(Page):
#     templates = 'tech_blog/article_listing_page.html'
#     max_count = 1


#Creting a snippet for categories
@register_snippet
class Category(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Título categoría', default='new category')
    slug = models.SlugField(
        verbose_name='nombre amigable',
        default='nueva categoría',
        allow_unicode=True,
        max_length=255,
        help_text='Es un nombre mas facil de recordar para las categorías',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]
    
    
    #get name of the category
    def __str__(self):
        
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering=['name']
   
#creating article Detail Page
class ArticleDetailPage(Page):
    templates = 'tech_blog/article_detail_page.html'
    # Article detail Page
    custom_title = models.CharField(
    max_length=100,
    blank=False,
    null=False,
    help_text='Overwrites the default title',
    verbose_name="Titulo del artículo"
    )
    # Article can have many categories

    categories = ParentalManyToManyField(Category, verbose_name='Categoría', blank=True)
    article_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name='Imagen del Artículo'
    )

    content = RichTextField( blank=True, null=True, verbose_name='Contenido' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
           FieldPanel("categories", widget=forms.CheckboxSelectMultiple ),
        ]),        
        ImageChooserPanel("article_image"),
        FieldPanel("content")

    ]
    # #get title of the articule
    # def __str__(self):
        
    #     return self.custom_title
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos' 


    def get_context(self, request, *args, **kwargs):
        # Adding custom to our context
        context = super().get_context(request, *args, **kwargs)
        # getting the list of Articles that are live and public 
        context["categories"] = Category.objects.all()
        return context

#widget=forms.CheckboxSelectMultiple

