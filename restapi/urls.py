from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from serviceapp.api import ProductResource

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())

urlpatterns = [
	url(r'^serviceapp/', include('serviceapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^/api/v1/product/search/', include('haystack.urls'))

]



