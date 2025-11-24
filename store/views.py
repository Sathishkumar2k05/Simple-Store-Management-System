from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Order, OrderItem

class HomeView(View):

    def get(self, request):

        context = {
            "products":Product.objects.all(),
            "orders":Order.objects.order_by('-created_at')
        }

        return render(request, 'home.html', context)
    
    def post(self, request):

        order = Order.objects.create()

        for key,value in request.POST.items():

            if key.startswith("qty_") and value:

                qty = int(value)

                if qty>0:

                    pid = key.split("_")[1]

                    product = Product.objects.get(id = pid)

                    OrderItem.objects.create(order = order, product = product, quantity = qty)

        return redirect("home")
