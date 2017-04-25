from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie.resources import fields
from tastypie.api import Api
from django.conf.urls import url
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from haystack.query import SearchQuerySet
from tastypie.utils import trailing_slash
from .models import Product


class ProductResource(ModelResource):
    product_id = fields.CharField(attribute='product_id')
    product_name = fields.CharField(attribute='product_name')
    product_url = fields.CharField(attribute='product_url')
    advertiser = fields.CharField(attribute='advertiser')
    designer = fields.CharField(attribute='designer')
    image_url = fields.CharField(attribute='image_url')
    price = fields.CharField(attribute='price')
    commission = fields.CharField(attribute='commission')

    class Meta:
        queryset = Product.objects.all().distinct()
        queryset = Product.objects.all()
        resource_name = 'product'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'product_id': ALL_WITH_RELATIONS, 
            'product_name': ALL_WITH_RELATIONS,
            'product_url': ALL_WITH_RELATIONS,
            'advertiser': ALL_WITH_RELATIONS,
            'designer': ALL_WITH_RELATIONS,
            'image_url': ALL_WITH_RELATIONS,
            'price': ALL_WITH_RELATIONS,
            'commission': ALL_WITH_RELATIONS
        }

    def prepend_urls(self):
        return [
        url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        sqs = SearchQuerySet().models(Product).load_all().auto_query(request.GET.get('keywords', ''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


v1_api = Api(api_name='v1')
v1_api.register(ProductResource())