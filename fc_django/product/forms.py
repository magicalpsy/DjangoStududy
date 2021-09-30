from django import forms
from .models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            "required": "상품명을 입력해 주세요",
        },
        max_length=64,
        label="상품명",
    )
    price = forms.IntegerField(
        error_messages={
            "required": "상품가격을 입력해 주세요",
        },
        # max_length=16,
        label="상품가격",
    )
    description = forms.CharField(
        error_messages={
            "required": "상품내용을 입력해 주세요",
        },
        label="상품내용",
    )
    stock = forms.IntegerField(
        error_messages={
            "required": "상품재고을 입력해 주세요",
        },
        # max_length=16,
        label="상품재고",
    )

    def clean(self):
        clean_data = super().clean()
        name = clean_data.get("name")
        price = clean_data.get("price")
        stock = clean_data.get("stock")
        description = clean_data.get("description")

        if name and price and description and stock:
            product = Product(
                name=name, price=price, stock=stock, description=description
            )
            product.save()
