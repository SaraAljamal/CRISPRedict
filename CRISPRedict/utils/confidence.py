import numpy as np

def mc_confidence(model, X_seq, X_num, n_iter=30):
    predictions = []

    for _ in range(n_iter):
        prediction = model([X_seq, X_num], training=True).numpy()
        predictions.append(prediction)

    predictions = np.array(predictions)
    mean = predictions.mean(axis=0)
    std = predictions.std(axis=0)
    return mean, std