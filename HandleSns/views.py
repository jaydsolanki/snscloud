from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, "index.html")


@csrf_exempt
def data(request):
    if request.method=="GET":
        return  render(request, "index.html")
    else:
        print (request.POST)
        return  render(request, "data.html", {"post_params": str(request.POST)})