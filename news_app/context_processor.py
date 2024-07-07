from .models import News, Category

def latest_news(request):
    latest = News.published.all().order_by("-published_at")[:10]
    categories = Category.objects.all()
    return {"latest_news": latest, "categories":categories}