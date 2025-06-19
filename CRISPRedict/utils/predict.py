import numpy as np 

def predict_on_target(model, seq_array, feature_array):

    seq_input = np.expand_dims(seq_array, axis=0)        
    num_input = np.expand_dims(feature_array, axis=0)  

    prediction = model.predict({'seq_input': seq_input, 'num_input': num_input})
    return prediction[0][0]