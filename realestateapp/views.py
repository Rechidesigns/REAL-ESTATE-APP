from django.shortcuts import render
from .models import Listing
from .forms import listingForm
# Create your views here.

def listing_list(request):
    Listings = Listing.objects.all()
    context = {'listings': Listings}
    return render(request, 'listings.html', context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {'listing': listing}
    return render(request, 'listing.html', context)


def listing_create(request):
    form = listingForm()
    if request.method == 'POST':
        form = listingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # TODO
            pass

    context = {'form': form} 
    return render(request, 'listing_create.html', context)