from django.apps import AppConfig
import tensorflow as tf
import os

class MlApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ml_api'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "good_enough_model.keras")
    model = tf.keras.models.load_model(model_path)
