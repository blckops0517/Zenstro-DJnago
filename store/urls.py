
from django.urls import path
from . import views


urlpatterns = [
    path("",views.store,name='store'),
    path("category/<slug:category_slug>/",views.store,name='products_by_category'), 
    # path for single page product
    path("category/<slug:category_slug>/<slug:product_slug>/",views.product_detail,name='product_detail'), 
    # path for search functionality
    path('search/',views.search,name='search'),
    
    # for review 
    path("submit_review/<int:product_id>/",views.submit_review,name="submit_review"),
   
   
]
