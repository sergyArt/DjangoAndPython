from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import Product


class ProductSerializer(ModelSerializer):

    category_id = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'article', 'country',
                  'pakaging', 'figure', 'image',
                  'category_id', 'url'
        ]

    def get_category_id(self, obj):
        return obj.category_id.name