from django.apps import AppConfig
import tensorflow as tf
import os
from ml_api.helper.parse_pbtxt import parse_pbtxt_file

class MlApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ml_api'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, "good_enough_model.keras")
    label_path = os.path.join(BASE_DIR, "bawang_label_map.pbtxt")
    model = tf.keras.models.load_model(model_path)
    label_map = parse_pbtxt_file(label_path)
    class_mapping = {item['id']: item['display_name'] for item in label_map}
