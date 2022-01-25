from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'), #this url will then be /lisitings
    path('<int:listing_id>', views.listing, name='listing'), #see how we have made a path parameter 'path' here!
    path('search', views.search, name='search'), #this url will be /listings/search
]
