from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article-details.html", views.articledetail, name="article-details"),
    path("privacy-policy.html", views.privacypolicy, name="privacy-policy"),
    path("terms-conditions.html", views.termsconditions, name="terms-conditions"),


    path("log-in.html", views.login_user, name="log-in"),
    path("logout_user", views.logout_user, name="log-out"),
    path("sign-up.html", views.signup_user, name="sign-up"),



]