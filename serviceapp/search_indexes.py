from haystack import indexes

from .models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    product_id = indexes.CharField(model_attr='product_id')
    product_name = indexes.CharField(model_attr='product_name')
    product_url = indexes.CharField(model_attr='product_url')
    advertiser = indexes.CharField(model_attr='advertiser')
    designer = indexes.CharField(model_attr='designer')
    image_url = indexes.CharField(model_attr='image_url')
    price = indexes.CharField(model_attr='price')
    commission = indexes.CharField(model_attr='commission')

    def get_model(self):
        return Product