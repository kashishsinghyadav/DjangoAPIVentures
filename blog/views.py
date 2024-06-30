from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests


# Create your views here.
def helloworld(request):
    url = "https://real-time-amazon-data.p.rapidapi.com/search"
    querystring = {"query":"Phone","page":"1","country":"US","category_id":"aps"}

    headers = {
	"X-RapidAPI-Key": "55bf7ea8bbmsh50ac1576f0dcf48p1c6b41jsn05c690cab719",
	"X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
}


    respon=requests.get(url,headers=headers,params=querystring)
    data=respon.json()
    return JsonResponse(data)

def numberofstudent(request):
    url="https://jsonmock.hackerrank.com/api/universities"
    res=requests.get(url)
    data=res.json()["data"]
    return JsonResponse(data,safe=False)

def quotes(request):
    url="https://zenquotes.io/api/random"
    res=requests.get(url).json()
    ans=res[0]
    return render(request,'quo.html',{'ans':ans})

