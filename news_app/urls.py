from django.urls import path
from .views import (
    news_list,
    detail_page,
    index,
    page404,
    contact_us,
    about,
    categories
)

urlpatterns = [
    path("news/<slug:slug>/", detail_page, name="detail_page"),
    path("news_list", news_list, name="news_list"),
    path("", index, name="home"),
    path("404-page-not-found/", page404, name="404"),
    path("contact-us/", contact_us, name="contact"),
    path("about/", about, name="about"),
    path("news/category/<slug:category>/", categories, name="categories"),
]
