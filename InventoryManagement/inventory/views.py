from django.shortcuts import render, redirect
from .models import Inventory, Supplier
from django.http import HttpResponse
from .serializers import SupplierSerializer, InventorySerializer
from rest_framework import viewsets


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# Create your views here.
def home(request):
    inventory = Inventory.objects.all()
    supplier = Supplier.objects.all()
    context = {
        'inventory': inventory,
        'supplier': supplier,
    }
    return render(request, 'home.html', context)
