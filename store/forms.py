# THIS FORM FOR REVIEW RATING PRODUCTS

from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model   = ReviewRating
        fields  = ['subject','review','rating'] 
 