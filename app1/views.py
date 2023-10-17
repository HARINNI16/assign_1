from django.shortcuts import render
import requests
def base(request):
    response=requests.get('https://jsonplaceholder.typicode.com/photos').json()

    return render(request, 'base.html',{'response':response})
    
# Create your views here.
