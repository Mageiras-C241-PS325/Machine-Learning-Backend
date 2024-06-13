from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from django.conf import settings  
from .apps import MlApiConfig
from django.http import HttpResponse, JsonResponse
import tensorflow as tf
import base64

# Create your views here.
@api_view(["POST"])
def predict(request):
    model = MlApiConfig.model
    file = request.data['file'] # is in base64 format
    # Convert to image
    image = base64.b64decode(file, validate=True)
    # Convert to tensor
    tensor = tf.image.decode_image(image)
    # Resize the image
    tensor = tf.image.resize(tensor, [640, 640])
    tensor = tf.expand_dims(tensor, 0)

    prediction = model.predict(tensor)
    
    return HttpResponse(prediction['classes'])
