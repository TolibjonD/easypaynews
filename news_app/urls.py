from django.urls import path
from .views import (
    news_list,
    detail_page,
    index,
    page404,
    contact_us,
    about,
    categories, 
    delete_news, 
    create_news,
    edit_news,
)

urlpatterns = [
    path("news/<slug:slug>/", detail_page, name="detail_page"),
    path("news_list", news_list, name="news_list"),
    path("news/create", create_news, name="create_news"),
    path("news/edit/<slug:slug>/", edit_news, name="edit_news"),
    path("", index, name="home"),
    path("404-page-not-found/", page404, name="404"),
    path("contact-us/", contact_us, name="contact"),
    path("about/", about, name="about"),
    path("news/category/<slug:category>/", categories, name="categories"),
    path("news/delete/<slug:slug>/", delete_news, name="delete_news"),
]
