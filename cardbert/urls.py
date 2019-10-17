from django.urls import path
from cardbert import views

urlpatterns = [
    path('card/<str:creditcard_number>', views.card_parse),
    path('card/random/<str:network>', views.card_random),
    path('card/random/', views.card_random),
]
