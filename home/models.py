from contextlib import redirect_stdout
from django.db import models
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from tech_blog.models import ArticleDetailPage
from tech_blog.models import Category

class HomePage(RoutablePageMixin, Page):
    templates = 'templates/home/home_page.html'
    max_count = 1
    # List all the articles detail pages

    created_at = models.DateTimeField(auto_now_add=True)

    #making search bar works
    # def search(self, request):
        
    #     result_query = 
    #     return result_query

    def get_context(self, request, *args, **kwargs):
        # Adding variables to our context
        context = super().get_context(request, *args, **kwargs)
        #check if there is a search request
        if request.method == "POST":
        #yes filter the post
            search_bar = request.POST.get('search_nav')
            all_post = ArticleDetailPage.objects.live().public().filter(custom_title__contains=search_bar).order_by('-first_published_at')
        #no get all the articles available
        else:
        # getting the list of Articles that are live and public 
            all_post = ArticleDetailPage.objects.live().public().order_by('-first_published_at')

        #making the paginate think work
        paginator = Paginator(all_post, 2) #change to 5 post
        page = request.GET.get("page")

        #handing errors
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context["posts"] = posts
        context["categories"] = Category.objects.all()

        return context
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    
    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="Categories")
    def Categories(self, request, cat_slug):
        # Adding variables to our context
        context = super().get_context(request)

        try:
            category = Category.objects.get(slug=cat_slug)
        except:
            category = None
        if category is None:
            redirect('home/home.html')

        all_post = ArticleDetailPage.objects.live().public().filter(categories__in=[category]).order_by('-first_published_at')
        

        paginator = Paginator(all_post, 2) #change to 5 post
        page = request.GET.get("page")

        #handing errors
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context["posts"] = posts
        context["categories"] = Category.objects.all()
        context["active_cat"] = cat_slug
        # context["categories"] = Category.objects.all()

        return render(request, 'home/home_page.html', context)