from django.core.management.base import BaseCommand
from products.models import Product, Description, Package
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'products/fixtures/data'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):

        product = load_from_json('product')
        Product.objects.all().delete()

        for prod in product:
            new_product = Product(**prod)
            new_product.save()

        description = load_from_json('description')
        Description.objects.all().delete()

        for pr_desc in description:
            prod_description = product['article']
            _prod = Description.objects.get(article=prod_description)
            product['description'] = _prod
            new_prod = Description(**product)
            new_prod.save()

        super_user = User.objects.create_superuser('admin','', 'pass')