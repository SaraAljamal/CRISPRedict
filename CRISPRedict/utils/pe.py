from keras.saving import register_keras_serializable
import tensorflow as tf
from tensorflow.keras.layers import Embedding

seq_len = 20        
d_model = 16 

position_embed = Embedding(input_dim=seq_len, output_dim=d_model)

@register_keras_serializable()
def add_positional_encoding(t):
    pe = position_embed(tf.range(seq_len))  
    return t + tf.expand_dims(pe, 0)