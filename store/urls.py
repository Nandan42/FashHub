"""WASP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('eventform/',views.eventform,name='eventform'),
    path('eventpage/',views.eventpage,name='eventpage'),
    path('event/<int:id>',views.event,name='event'),
    path('journal/',views.journal,name='journals'),
    path('journal/<int:id>',views.journal_page,name='journal_page'),
    path('products/<int:id>/',views.product,name='product'),
    path('cart/',views.showcart,name='cart'),
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('buy/<int:id>',views.buy,name='buy'),
    path('buycart/',views.buycart,name='buycart'),
    path('showWishlist/',views.showWishlist,name='showWishlist'),
    path('addWishlist/<int:id>',views.addWishlist,name='addWishlist'),
    path('removeWishlist/<int:id>',views.removeWishlist,name='removeWishlist'),
    path('donation/',views.donation,name='donation'),
    path('products/<str:gender>/<str:category>',views.genderCategory,name='genderCategory'),
    path('aboutus/',views.aboutus,name='aboutus'),
    # path('<str:gender>/<str:category>',views.,name='menbottom'),
    # path('<str:gender>/<str:category>',views.,name='menfootware'),
    # path('<str:gender>/<str:category>',views.,name='menaccessories'),
    # path('women/<str:category>',views.,name='womenshirt'),
    # path('women/bottom',views.,name='womenbottom'),
    # path('women/footware',views.,name='womenfootware'),
    # path('women/accessories',views.,name='womenaccessories'),
    # path('kids/shirt',views.,name='kidsshirt'),
    # path('kids/bottom',views.,name='kidsbottom'),
    # path('kids/footware',views.,name='kidsfootware'),
    # path('kids/accessories',views.,name='kidsaccessories'),
    # path('fluids/shirt',views.,name='fluidsshirt'),
    # path('fluids/bottom',views.,name='fluidsbottom'),
    # path('fluids/footware',views.,name='fluidsfootware'),
    # path('fluids/accessories',views.,name='fluidsaccessories'),
]
# shirt
# jeans
# footware
# sheatshirts
# jackets
# fitness
# tshirts
# ethnic


# men, women, kid, fluids