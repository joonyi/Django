from django.test import TestCase
from .models import Supplier, Inventory

# Create your tests here.
class SupplierTests(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="KFC")

    def test_api_page_status_code(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)

    def test_api_supplier_status_code(self):
        response = self.client.get("/api/supplier/")
        self.assertEqual(response.status_code, 200)

    def test_supplier_id_status_code(self):
        response = self.client.get("/api/supplier/1/")
        self.assertEqual(response.status_code, 200)


class InventoryTests(TestCase):
    def setUp(self):
        self.inventory = Inventory.objects.create(
            name="Volcano Roll",
            description="Food",
            note="hot",
            stock=3,
            availability="True",
            supplier=Supplier.objects.create(name="KFC")
        )

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_inventory_page_status_code(self):
        response = self.client.get("/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_api_inventory_status_code(self):
        response = self.client.get("/api/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_inventory_id_status_code(self):
        response = self.client.get("/api/inventory/1/")
        self.assertEqual(response.status_code, 200)
