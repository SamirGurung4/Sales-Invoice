from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.forms import inlineformset_factory, BaseInlineFormSet
from .forms import InvoiceForm, InvoiceItemForm
from .models import Invoice, InvoiceItem, Customer


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'
    context_object_name = 'invoices'


class CreateInvoiceView(FormView):
    template_name = 'invoice.html'
    form_class = InvoiceForm
    success_url = 'invoice_list/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, formset=InvoiceItemFormSet,
                                                   fields=('Product', 'Quantity'))
        data['formset'] = InvoiceItemFormset(self.request.POST or None)
        return data

    def form_valid(self, form):
        customer_name = self.request.POST.get('Customer_name')

        # Get or create the customer
        customer, created = Customer.objects.get_or_create(Name=customer_name)

        # Save the invoice with the customer
        invoice = form.save(commit=False)
        invoice.Customer = customer
        invoice.save()

        # Process the formset data
        InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm)
        formset = InvoiceItemFormset(self.request.POST, instance=invoice)

        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)

        return self.form_invalid(form)

    def form_invalid(self, form):
        formset_class = inlineformset_factory(Invoice, InvoiceItem, formset=InvoiceItemFormSet,
                                              fields=('Product', 'Quantity'))
        formset = formset_class(self.request.POST, self.request.FILES)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class InvoiceItemFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # Add custom validation for the formset if needed
