from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        labeel = {
            "product_id": "Product ID",
            "name": "Name",
            "sku": "SKU",
            "quantity": "Quantity",
            "supplier": "Supplier",
        }
        widgets = {
            "product_id": forms.NumberInput(
                attrs={"placeholder": "e.g 1", "class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"placeholder": "e.g shirt", "class": "form-control"}
            ),
            "sku": forms.TextInput(
                attrs={"placeholder": "e.g 13445", "class": "form-control"}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "e.g 15.99", "class": "form-control"}
            ),
            "quantity": forms.NumberInput(
                attrs={"placeholder": "e.g 10", "class": "form-control"}
            ),
            "supplier": forms.TextInput(
                attrs={"placeholder": "e.g ABC Corp ", "class": "form-control"}
            ),
        }
