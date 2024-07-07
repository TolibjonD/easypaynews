from django.shortcuts import render, redirect
from .models import Category, News
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    categories = Category.objects.all()
    latest_news = News.published.all().order_by('-published_at')[:5]
    side_latest_news = News.published.all().order_by('-published_at')[5:15]
    first_category = categories[0]
    first_category_news = News.published.all().filter(category__name='Mahalliy')[:5]
    sport_news = News.published.all().filter(category__name='Sport')[:5]
    technology_news = News.published.all().filter(category__name='Texnologiya')[:5]
    abroad_news = News.published.all().filter(category__name='Xorij')[:5]
    first_category_single_post = News.published.all().filter(category__name="Mahalliy").order_by('-published_at')[0]
    context = {
        "categories": categories,
        "latest_news": latest_news,
        "first_category_news": first_category_news,
        "sport_news": sport_news,
        "technology_news": technology_news,
        "abroad_news": abroad_news,
        "single_post": first_category_single_post,
        "side_latest_news": side_latest_news
    }
    return render(request, "index.html", context)

def page404(request):
    return render(request, "pages/404.html")

def contact_us(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Murojaatingiz muvvaffaqiyatli yuborildi !")
        return redirect("contact")
    context = {
        "form": form
    }
    return render(request, "pages/contact.html", context)

def about(request):
    return render(request, "pages/about.html")

def news_list(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        "news": news,
        "categories": categories
    }
    return render(request, "news/news_list.html", context)

def detail_page(request, slug):
    news = News.published.filter(slug=slug)[0]
    categories = Category.objects.all()
    context = {
        "news": news,
        "categories": categories
    }
    return render(request, "news/detail.html", context)


def categories(request, category):
    category = Category.objects.get(name=category)
    news = News.objects.filter(category=category.id).order_by("-published_at")
    context = {
        "news": news,
        "category": category
    }
    return render(request, "pages/categories.html", context)