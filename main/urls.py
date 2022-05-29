from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article-details.html", views.articledetail, name="article-details"),
    path("log-in.html", views.login, name="log-in"),
    path("privacy-policy.html", views.privacypolicy, name="privacy-policy"),
    path("sign-up.html", views.signup, name="sign-up"),
    path("terms-conditions.html", views.termsconditions, name="terms-conditions"),
]