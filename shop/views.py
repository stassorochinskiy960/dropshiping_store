from django.shortcuts import render


def shop(request):
    return render(request, 'shop/shop.html')


def detail(request):
    return render(request, 'shop/detail.html')
