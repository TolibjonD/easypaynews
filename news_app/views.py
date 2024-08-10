from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Category, News
from .forms import ContactForm, NewsForm
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

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
    photographs = News.published.all()[:6]
    context = {
        "categories": categories,
        "latest_news": latest_news,
        "first_category_news": first_category_news,
        "sport_news": sport_news,
        "technology_news": technology_news,
        "abroad_news": abroad_news,
        "single_post": first_category_single_post,
        "side_latest_news": side_latest_news,
        "photographs": photographs
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
    related_news = News.published.filter(Q(category=news.category)).exclude(id=news.id)[:3]
    categories = Category.objects.all()
    try:
        previous_news = News.published.filter(Q(category=news.category) and Q(id=int(news.id-1)))[0]
    except:
        previous_news=0
    try:
        next_news = News.published.filter(Q(category=news.category) and Q(id=int(news.id+1)))[0]
    except:
        next_news=0
    latest_news = News.published.all().order_by('-published_at')[:4]
    context = {
        "news": news,
        "categories": categories,
        "previous_news": previous_news,
        "next_news": next_news,
        "related_news": related_news,
        "latest_news": latest_news
    }
    return render(request, "pages/single_page.html", context)


def categories(request, category):
    category = Category.objects.get(name=category)
    news = News.objects.filter(category=category.id).order_by("-published_at")
    context = {
        "news": news,
        "category": category
    }
    return render(request, "pages/categories.html", context)

def delete_news(request, slug):
    news = News.published.get(slug=slug)
    category = news.category
    news.delete()
    return redirect(reverse("categories", kwargs={"category": category}))


def create_news(request):
    form=NewsForm()
    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "news/create_news.html", {"form": form})
    return render(request, "news/create_news.html", {"form": form})

def edit_news(request, slug):
    news = News.published.get(slug=slug)
    form=NewsForm(instance=news)
    if request.method == 'POST':
        form = NewsForm(instance=news,data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save()
            slug = news.slug
            return redirect(reverse("detail_page", kwargs={"slug": slug}))
        else:
            return render(request, "news/create_news.html", {"form": form})
    return render(request, "news/edit_news.html", {"form": form})