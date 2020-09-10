from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from cart.forms import CartAddProductForm

import os


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    cart_product_form = CartAddProductForm()
    cart_product_form.fields['quantity'].initial = 1

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/list.html', {'category': category,
                                              'categories': categories,
                                              'products': products,
                                              'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'product': product,
                                                'cart_product_form': cart_product_form})
