from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
# from FiveFingerDiscountAPI import views
from cards import views as CardViews
from games import views as GameViews
from phases import views as PhaseViews
from players import views as PlayerViews
from scores import views as ScoreViews
from turns import views as TurnViews

urlpatterns = [
    url(r'^cards/$', CardViews.CardList.as_view()),
    url(r'^cards/(?P<pk>[0-9]+)/$', CardViews.CardDetail.as_view()),

    url(r'^games/$', GameViews.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', GameViews.GameDetail.as_view()),

    url(r'^phases/$', PhaseViews.PhaseList.as_view()),
    url(r'^phases/(?P<pk>[0-9]+)/$', PhaseViews.PhaseDetail.as_view()),

    url(r'^players/$', PlayerViews.PlayerList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)/$', PlayerViews.PlayerDetail.as_view()),

    url(r'^scores/$', ScoreViews.ScoreList.as_view()),
    url(r'^scores/(?P<pk>[0-9]+)/$', ScoreViews.ScoreDetail.as_view()),

    url(r'^turns/$', TurnViews.TurnList.as_view()),
    url(r'^turns/(?P<pk>[0-9]+)/$', TurnViews.TurnDetail.as_view()),
]
