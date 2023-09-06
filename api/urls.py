from django.urls import path
from .import views as apiviews

urlpatterns = [
    path('products/<int:product_id>/refill', apiviews.RefillProductView, name='refill_product_view'),
    path('add/products/', apiviews.AddNewProductView, name='product_add_view'),
    path('purchases/', apiviews.PurchaseView.as_view(), name='purchase-list'),
    path('api/export/products/', apiviews.ExportPurchaseCsv.as_view(),name='purchase_csv_export'),
]
