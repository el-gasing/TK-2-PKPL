from django.urls import path

from .views import edit_theme, home, quick_login

urlpatterns = [
    path("", home, name="home"),
    path("login/", quick_login, name="quick_login"),
    path("tema/", edit_theme, name="edit_theme"),
]
