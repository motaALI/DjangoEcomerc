from django.urls import path, include

from product import views

urlpatterns = [
    path('latest_products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDitail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    
]