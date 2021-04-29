from django.shortcuts import render
import requests
import json


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
#
headers = {
    'x-rapidapi-key': "c11e37766amshec2677cc21bbd65p16f04ejsn2b39e3b52521",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
# url = "https://covid-193.p.rapidapi.com/statistics"
#
# headers = {
#     'x-rapidapi-key': "c11e37766amshec2677cc21bbd65p16f04ejsn2b39e3b52521",
#     'x-rapidapi-host': "covid-193.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers).json()
empty_string = ''

def is_valid_params(param):
    return param!=empty_string and param is not None

def helloworldview(request):
    noofresults = response['state_wise']

    which_data=''
    # print(noofresults)
    # print(len(noofresults))

    states=[str(st) for st in noofresults]
    districts=[]
    for state in states:
        for dist in noofresults[state]['district']:
            districts.append(dist)


    context={
        # 'sam':noofresults['Maharashtra']['district']['Ahmednagar'],
        'states':states,
        'districts':districts,
    }

    input_state = request.GET.get('state')
    input_district = request.GET.get('district')

    data=None
    if is_valid_params(input_state) and is_valid_params(input_district):
        data=noofresults[input_state]['district'][input_district]
        which_data+=input_state+","+input_district
    elif is_valid_params(input_state):
        data=noofresults[input_state]['district']
        which_data += input_state
    context['data']=data
    if is_valid_params(which_data):
        context['which_data']=which_data
    return render(request,'hello.html',context)