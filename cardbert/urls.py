# from django.contrib import admin
from django.urls import path
from cardbert import views

urlpatterns = [
    # path('card', views.card_parse),
    path('card/<str:creditcard_number>',  views.card_parse),
    # path('card/(P<cc>\w+)', views.card_parse), # TODO use this instead? #https://stackoverflow.com/a/150518
    path('card/random',  views.card_random),
]
