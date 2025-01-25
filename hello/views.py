from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import countries

def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})

def get_countries(request):
    countries_name = []
    for country in countries:
        countries_name.append(country["country"])
    return JsonResponse({"data":countries_name})

@csrf_exempt
def post_country_population(request):
    data = json.loads(request.body)
    for country in countries:
        if country['country'] == data.get('country', ''):
            return JsonResponse({"data":country["population"]})
    return JsonResponse({"data":""})

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name', 'No name provided')
            age = data.get('age', 'No age provided')

            return JsonResponse({
                'message': 'Data received successfully',
                'name': name,
                'age': age
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

