from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from django.conf import settings  
from .apps import MlApiConfig
from django.http import HttpResponse, JsonResponse
import tensorflow as tf

# Create your views here.
@api_view(["GET"])
def ping(request):
    model = MlApiConfig.model
    # Get model's input shape
    random_tensor = tf.random.normal([1, 640, 640, 3])
    # Make a prediction
    prediction = model.predict(random_tensor)
    print(prediction)
    return HttpResponse(prediction['classes'])
