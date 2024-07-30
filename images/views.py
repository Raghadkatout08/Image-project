from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Food
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def food_view(request):
    api_key = settings.PIXABAY_API_KEY
    url = f"https://pixabay.com/api/?key={api_key}&category=food"
    response = requests.get(url)
    data = response.json()
    api_data = data.get('hits', [])

    existing_ids = set(Food.objects.values_list('id', flat=True))

    new_records = []


    for food in api_data:
        if food['id'] not in existing_ids:
            new_records.append(Food(
                id=food['id'],
                largeImageURL=food['largeImageURL'],
                tags=food['tags'],
                views=food['views'],
                downloads=food['downloads'],
                collections=food['collections'],
                likes=food['likes'],
                comments=food['comments'],
                user=food['user'],
                userImageURL=food['userImageURL']
            ))

    if new_records:
        Food.objects.bulk_create(new_records)

    food_items = Food.objects.all().values()
    food_list = list(food_items)
    # return JsonResponse({'obj': food_list})
    return render(request, 'image_list.html', {'images': food_list})

def food_details_view(request, pk):
    food = get_object_or_404(Food, id=pk)
    return render(request, 'image_detail.html', {'image': food})