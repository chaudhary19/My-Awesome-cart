from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shophome'),
    path('About/',views.About,name='AboutUs'),
    path('Contact/',views.Contact,name='ContactUs'),
    path('Tracker/',views.Tracker,name='Tracker'),
    path('search/',views.Search,name='Search'),
    path('ProductView/',views.Productview,name='ProductView'),
    path('Checkout/',views.Checkout,name='Checkout'),
    path('Product/',views.Productlist,name='product Items'),
]
