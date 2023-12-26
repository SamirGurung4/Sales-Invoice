from django.urls import path
from .views import InvoiceListView, CreateInvoiceView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('create_invoice/', CreateInvoiceView.as_view(), name='new_invoice'),
]

