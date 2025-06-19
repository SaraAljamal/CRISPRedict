from tensorflow.keras.models import load_model
from utils.pe import add_positional_encoding

def load_model_keras(cell_line):
    model_path = f"models/{cell_line}_model.keras"
    if cell_line=='hl60': # Without attention  
        return load_model(model_path)
    else:
        return load_model(model_path, custom_objects={"add_positional_encoding": add_positional_encoding})