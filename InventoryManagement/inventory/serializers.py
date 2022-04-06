from inventory.models import Supplier, Inventory
from rest_framework_json_api import serializers


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name', 'inventory_set')


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')
        # fields = ('name', 'description', 'note', 'stock', 'availability', 'supplier')
