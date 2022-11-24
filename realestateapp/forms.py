from django.forms import ModelForm
from .models import Listing


class listingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "numbers_of_bedrooms",
            "numbers_of_bathrooms",
            "square_footage",
            "address",
        ]