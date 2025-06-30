from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializer import FoodSerializer
from modelFood.models import Food
from models.models import Contact

# Create your views here.
def allFoods(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods,many=True)

    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        description = data.get("description")

        contact = Contact(name=name,email=email,phone_number=phone,description=description)
        contact.save()

        return JsonResponse({'success':True})
    
    else:
        return JsonResponse({'success':False,'message':'Invalid request method'})

