from django.shortcuts import render
# from django.http import HttpResponse
import json
import urllib.request
# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = 'cc1f71266946419a8ce52142201410'
        source = urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+city).read()
        list_of_data = json.loads(source)
        print(list_of_data)
        data={
            'name': str(list_of_data['location']['name']),
            'coordinates':{
                'longitude': str(list_of_data['location']['lon']),
                'latitude': str(list_of_data['location']['lat']),
            },
            'pressure': str(list_of_data['current']['pressure_mb']),
            'humidity': str(list_of_data['current']['humidity']),
            'wind': str(list_of_data['current']['wind_kph']),
            'temp_f': str(list_of_data['current']['temp_f']),
            'text': str(list_of_data['current']['condition']['text']),
            'local_time': str(list_of_data['location']['localtime']),
        }
    else:
        data={}   
    return render(request, 'weather.html', data)