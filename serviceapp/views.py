from django.shortcuts import render, HttpResponse
import requests, json, hashlib
from six.moves.urllib.parse import urlparse, urlunparse, parse_qs
import urllib
from xml.etree import ElementTree
from .models import Product

def index(request):
        return render(request, 'base.html')

def encryptMd5Hash(string):
    m= hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def rewardstyle(request):
    if request.method == 'POST':
        advertiserName = request.POST.get('advertiserName')
        getProdcuts(advertiserName)
    parsedData = []
    req = requests.get('https://api.rewardstyle.com/v1/advertisers?oauth_token=b0971cc14df1152194c7c9a4e72cf297')
    jsonList = []
    jsonList.append(json.loads(req.content.decode()))
    advertiserData = {}
    for data in jsonList:
        advertiserData['advertiser'] = data['advertisers']
    parsedData.append(advertiserData)
    return render(request, 'serviceapp/rewardstyle.html', {'data': parsedData})  
    

def getProdcuts(advertiserName):
    token = 'b0971cc14df1152194c7c9a4e72cf297'
    tokenHashed = encryptMd5Hash(token)
    url = 'https://api.rewardstyle.com/v1/product_feed?advertiser='+advertiserName+'&oauth_token='+token
    xml = requests.get(url, stream=True)
    tree = ElementTree.parse(xml.raw)
    for item in tree.iter('item'):
        product_id =  item.find('product_id').text
        product_name = item.find('product_name').text
        product_url = item.find('product_url').text
        parsed = urlparse(product_url)
        qs = parse_qs(parsed.query)
        qs['t'] = [tokenHashed]
        newqs = urllib.parse.urlencode(qs, doseq=1)
        newurl = urlunparse([newqs if i == 4 else x for i,x in enumerate(parsed)])
        advertiser = item.find('advertiser').text
        designer = item.find('designer').text
        image_url = item.find('image_url').text
        price = item.find('price').text
        commission = item.find('commission').text
        product_to_save = Product.objects.create(product_id=product_id, product_name=product_name, product_url=newurl, advertiser=advertiser, designer=designer, image_url=image_url, price=price, commission=commission)
        product_to_save.save()
    return HttpResponse()





