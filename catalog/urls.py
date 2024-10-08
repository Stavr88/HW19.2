from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contacts, product_detail

app_name = CatalogConfig.name
urlpatterns = [
    path("", products_list, name="products_list"),
    path("catalog/<int:pk>/", product_detail, name="product_detail"),
    path("contacts/", contacts, name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
