from django.shortcuts import render
import requests

# Create your views here.
def homepage(req):
    return render(req,'index.html')

def store(req):
    response = requests.get('https://dummyjson.com/products?limit=0')
    data = response.json()
    print(data)
    return render(req,"store.html",context={"data":data['products']})