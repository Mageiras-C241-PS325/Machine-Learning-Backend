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
    try:
        file = request.data['file']  # is in base64 format
        # Convert to image
        image = base64.b64decode(file, validate=True)
        # Convert to tensor
        tensor = tf.image.decode_image(image)
    except:
        return JsonResponse({"error": "Invalid file"}, status=400)
    # Resize the image
    tensor = tf.image.resize(tensor, [640, 640])
    tensor = tf.expand_dims(tensor, 0)

    prediction = list(model.predict(tensor)['classes'][0])
    class_mapping = MlApiConfig.class_mapping
    mapped_classes = [class_mapping[class_num] for class_num in prediction if class_num in class_mapping.keys()]
    mapped_classes = ";".join(mapped_classes) if mapped_classes else "No prediction"
    return HttpResponse(mapped_classes)
