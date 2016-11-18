from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import urllib2
import json

def index(request):
    return render(request, "index.html")


@csrf_exempt
def data(request):
    if request.method=="GET":
        return  render(request, "index.html")
    else:
        headers = json.loads(request.body)
        # print(request.body)
        print("Seriving POST Request")
        if 'Type' in headers.keys():
            if headers['Type']=="SubscriptionConfirmation":
                print("Got COnfirmation Request") 
                subscribeUrl = headers['SubscribeURL']
                responseData = urllib2.urlopen(subscribeUrl).read()
                print(responseData)
            elif headers['Type']=="Notification":
                print ("Got a new Message")
                message = json.loads(headers["Message"])
                print (message)
        return  render(request, "data.html", {"post_params": str(request.POST)})
