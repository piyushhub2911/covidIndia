from django.shortcuts import render
import requests
import json


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "c11e37766amshec2677cc21bbd65p16f04ejsn2b39e3b52521",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json


def helloworldview(request):
    mylist = []
    noofresults = int(response['response'])
    for x in range(0,noofresults):
        mylist.append([x])
        context={'mylist':mylist}
        return render(request,'hello.html',context)
    return render(request,'hello.html',context)