import streamlit as st
import numpy as np
from utils.preprocessing import load_prep_files, handle_seq, one_hot_encode, gc_content, scale_gc_content, strand_transform
from utils.model_loader import load_model_keras
from utils.predict import predict_on_target
from utils.confidence import mc_confidence
import plotly.graph_objects as go

# App setup
st.set_page_config(page_title="🧬 CRISPRedict", layout="centered")
st.title("🧬 CRISPRedict")
st.markdown(
    "<p style='font-size:20px; color:white;'>A web tool for Predicting the On-target Efficacy of CRISPR sgRNA Sequences</p>",
    unsafe_allow_html=True
)

# Input
with st.sidebar:
    st.subheader("CRISPR Input Details")

    cell_line = st.selectbox("Choose Cell Line", ['hct116', 'hek293t', 'hela', 'hl60'])
    sequence_input = st.text_input("Enter sgRNA sequence (20bp + PAM) or without PAM:")
    strand = st.selectbox("Select Strand", ['+', '-'])
    chromosome = st.number_input("Enter Chromosome Number (For Chromosome X, please enter 23)", min_value=0, max_value=23, step=1)

    predict_button = st.button("Predict")

if predict_button:
    if sequence_input:

        # Preprocessing
        encoder, gc_scaler = load_prep_files(cell_line)
        cleaned_seq = handle_seq(sequence_input)
        if cleaned_seq is None: 
            st.stop() 
        input_seq = one_hot_encode(cleaned_seq, encoder)
        gc = gc_content(cleaned_seq)
        scaled_gc = scale_gc_content(cleaned_seq, gc_scaler)
        strand_trans = strand_transform(strand)
        feature_array = np.array([chromosome, strand_trans, scaled_gc], dtype=np.float32)

        # Load model and predict
        model = load_model_keras(cell_line)
        prediction = predict_on_target(model, input_seq, feature_array)
        seq_input = np.expand_dims(input_seq, axis=0)         # shape (1, 20, 4)
        num_input = np.expand_dims(feature_array, axis=0)
        mean_pred, std_pred = mc_confidence(model, seq_input, num_input, n_iter=30)

        st.header("Input Summary")
        st.write(f"**Selected Cell Line**: {cell_line}")
        st.write(f"**Input Sequence:** {cleaned_seq}")
        st.write(f"**Strand:** {strand}")
        st.write(f"**Chromosome:** {chromosome}")
        st.write("---")

        st.header("Results")
        col1, col2 = st.columns(2)

        # Column 1: Efficacy & Confidence 
        with col1:
            st.subheader("Efficacy")
            st.metric(label= 'Predicted On-Target Efficacy Score (Editing Effectiveness)', value=f"{prediction*100:.2f}%")
            st.progress(float(prediction))
            st.subheader("Confidence")
            
            std = std_pred.item()
            if std < 0.03:
                confidence = "High Confidence"
            elif std < 0.06:
                confidence = "Moderate Confidence"
            else:
                confidence = "Low Confidence"

            st.markdown(f"**The Model's Confidence of the prediction:**    \n{confidence}")

        # Column 2: GC Content
        with col2:
            st.subheader("GC Content")
            gc = float(gc)
            if gc > 1:
                gc /= 100.0
            at = 1 - gc

            st.metric(label='GC Content Percentage', value=f"{gc * 100:.2f}%")

            fig = go.Figure(data=[go.Pie(labels=['GC Content', 'AT Content'], values=[gc, at], hole=0.4,marker=dict(colors=["#2073D7", "#FDFEFF"]), textinfo='none', insidetextorientation='radial')])
            fig.update_layout(showlegend=True, height=200, margin=dict(t=5, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
     
    else:
        st.error("Please enter a valid sgRNA sequence.")
else:
    st.info("Enter the details in the sidebar and click 'Predict' to see the results.")