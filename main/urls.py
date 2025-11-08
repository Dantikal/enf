from django.urls import path
from . import views

app_name = '.mian'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalaog/', views.CatalogView.as_view(), name='catalog_all'),
    path('catalog/<slug:category_slug>/', views.CatalohgView.as_view(), name='catalog'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
]