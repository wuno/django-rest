from django.shortcuts import render
import requests
import json


def index(request):
        return render(request, 'serviceapp.html')


def tmdb(request):
        return render(request, 'serviceapp/tmdb.html')


def rewardstyle(request):
        return render(request, 'serviceapp/rewardstyle.html')        

def github(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content.decode()))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'serviceapp/github.html', {'data': parsedData})





