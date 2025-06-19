
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np
import joblib
import streamlit as st

def load_prep_files(cell_line):
    encoder_path = f"preprocessing/{cell_line}_encoder.pkl"
    scaler_path = f"preprocessing/{cell_line}_gc_minmax_scaler.pkl"

    encoder = joblib.load(encoder_path)
    gc_scaler = joblib.load(scaler_path)
    return encoder, gc_scaler

def handle_seq(seq):
    seq = seq.upper().replace("U", "T").strip()

    bases = {"A", "T", "C", "G"}
    if any(base not in bases for base in seq):
        st.error("Sequence must only contain A, T, C, G")
        return None
    
    if len(seq) == 20:
        return seq 
    
    elif len(seq) == 23:
        return seq[:-3]  
    
    else:
        st.error("Sequence length must be 20 (without PAM) or 23 (With PAM)")
        return None

def one_hot_encode(sequence, encoder):
    seq_arr = np.array(list(sequence)).reshape(-1, 1)
    mat= encoder.transform(seq_arr)
    arr=mat.toarray()
    return arr.astype(np.float32)

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

def scale_gc_content(seq, gc_scaler):
    gc_count= gc_content(seq)
    scaled_gc= gc_scaler.transform([[gc_count]])
    return float(scaled_gc[0][0])

def strand_transform(strand):
    strand_map = {'+': 0, '-': 1}
    return strand_map.get(strand) 

