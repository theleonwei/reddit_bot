from django.urls import path

from reddit_bot.reddit.views import lead_view

urlpatterns = [

    path("leads/", view=lead_view, name="leads"),

]
