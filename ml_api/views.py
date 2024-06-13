from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from django.conf import settings  
from .apps import MlApiConfig
from django.http import HttpResponse, JsonResponse
import tensorflow as tf

# Create your views here.
@api_view(["POST"])
def predict(request):
    model = MlApiConfig.model
    file = request.data['file']
    # Convert to tensor
    tensor = tf.image.decode_image(file.read())
    # Resize the image
    tensor = tf.image.resize(tensor, [640, 640])
    prediction = model.predict(tensor)
    
    return HttpResponse(prediction['classes'])
