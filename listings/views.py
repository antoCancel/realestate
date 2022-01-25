from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import state_choices, price_choices, bedroom_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    data = {
        'listings': paged_listings,
    }
    return render (request, 'listings/listings.html', data)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    data = {
        'listing': listing
    }
    return render (request, 'listings/listing.html', data)

def search(request):
    queryResult = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryResult = queryResult.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryResult = queryResult.filter(city__iexact = city)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryResult = queryResult.filter(bedrooms__lte = bedrooms)
    
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryResult = queryResult.filter(price__lte = price)

    data = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryResult,
        'values': request.GET,
    }

    return render (request, 'listings/search.html', data)