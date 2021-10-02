from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import (
    method_decorator,
)
from .forms import RegisterForm
from .models import Order
from fcuser.decorators import login_required

# Create your views here.
@method_decorator(login_required, name="dispatch")
class OrderCreate(FormView):
    context_object_name = "Order_Create"
    form_class = RegisterForm
    success_url = "/product/"

    def form_invalid(self, form):
        return redirect(
            "/product/" + str(form.product)
        )

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({"request": self.request})

        return kw


@method_decorator(login_required, name="dispatch")
class OrderList(ListView):
    model = Order
    template_name = "order.html"
    context_object_name = "order_list"

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get(
                "user"
            )
        )
        return queryset
