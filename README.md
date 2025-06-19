# CRISPRedict: A Deep Learning-Powered CRISPR-Cas9 On-target Efficacy Prediction

## Table of Contents
- [Overview](#overview)
- [Motivation](#motivation)
- [Key Features](#key-features)
- [How it Works](#how-it-works)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Overview

CRISPRedict is a web platform developed to predict the On-target efficacy of sgRNA sequences using advanced deep learning techniques. It takes input from the user such as the cell line, DNA sequence, chromosome number, and strand, in order to display a predicted efficacy score and more info. CRISPRedict is Designed to be used by genetic and bioengineers where the interface is clean, intuitive, with minimized technical complexity.

## Motivation

CRISPR-Cas9, while a revolutionary gene-editing technique, faces significant challenges related to its precision, particularly concerning unintended "Off-target" edits. The cornerstone to successful and safe gene editing lies in maximizing "On-target" efficiency. CRISPRedict directly addresses this critical need by:

- **Improving Efficacy Prediction:** Utilizing advanced deep learning models to provide more accurate and reliable On-target efficacy forecasts.
- **Enhancing Confidence:** Offering researchers a sophisticated tool to pre-screen sgRNA sequences, thereby increasing confidence in experimental design and outcomes.
- **Accelerating Research:** Streamlining the sgRNA selection process, reducing experimental cycles, and ultimately supporting the advancement of CRISPR technology.

By predicting On-target efficacy, CRISPRedict empowers researchers to explore how effectively a sequence will contribute to desired gene edits, mitigating risks and optimizing experimental success.

## Key Features

CRISPRedict offers a robust set of features designed for precision and ease of use:

-   **Cell Line Selection:** Choose from a variety of pre-trained cell-line specific models for tailored predictions.
-   **sgRNA Sequence Input:** Easily input your specific single-guide RNA sequence for evaluation.
-   **Contextual Data Input:** Provide essential details such as chromosome number and DNA strand (+/-) for comprehensive analysis.
-   **Deep Learning Prediction:** Utilizes powerful deep learning-based regression models to generate On-target efficacy scores.
-   **User-Friendly Interface:** A simple and intuitive web interface for seamless input and result visualization, powered by Streamlit.
-   **Detailed Output:** Displays clear efficacy predictions alongside additional informative metrics like GC content and model confidence.
-   **Robust Preprocessing:** Handles sequence validation, encoding, GC content calculation, scaling, and strand mapping internally.

## How it Works

CRISPRedict operates through a streamlined process:

1.  **User Input:** Users provide their sgRNA sequence, select a cell line, and specify chromosome/strand information via the web interface.
2.  **Preprocessing:** The input sequence undergoes thorough validation and preprocessing (e.g., one-hot encoding, GC content calculation, scaling) specific to the chosen cell line.
3.  **Model Inference:** The processed data is fed into a pre-trained deep learning regression model optimized for the selected cell line.
4.  **Prediction & Confidence:** The model predicts the On-target efficacy score. Concurrently, a confidence score for the prediction is calculated.
5.  **Result Display:** The predicted efficacy score, GC content, and model confidence are presented to the user through a clear and interactive UI.

## Project Structure

The project is structured to ensure modularity, scalability, and easy maintenance:

CRISPRedict/

├── App.py # Main Streamlit application entry point.

├── Models/ # Contains the final .keras model files, one for each specific cell line.

├── Utils/ # Core utility functions for the application.

│ ├── model_loader.py # Handles loading the appropriate Deep Learning model.

│ ├── pe.py # Positional Encoder module (likely for sequence features).

│ ├── predict.py # Contains logic for making predictions using loaded models.

│ ├── preprocessing.py # Manages input sequence handling, verification, encoding, GC calculation, scaling, and strand mapping.

│ └── confidence.py # Calculates and provides the model's confidence for a given prediction.

├── Preprocessing/ # Stores serialized preprocessors (.pkl files) for each cell line.

├── README.md # This file, providing project overview and instructions.

└── requirements.txt # Lists all necessary Python libraries and their versions.

Cell line testing/ # Contains Jupyter notebooks demonstrating model training and testing for each cell line.



## Technologies Used

-   **Python:** The core programming language for the entire application.
-   **Streamlit:** For building the interactive and user-friendly web interface.
-   **Deep Learning Framework:** Keras (running on TensorFlow or another backend) for building and deploying the predictive models.
-   **Data Science Libraries:** Likely includes NumPy, Pandas, Scikit-learn (for preprocessing utilities like scalers and encoders).

## Installation

To get CRISPRedict up and running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/project-name.git
    cd project-name
    ```
    *(Remember to replace `yourusername/project-name` with your actual GitHub repository link.)*

2. **Install dependencies:**
    All required libraries are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the dependencies are installed, you can launch the CRISPRedict web application:


1.  **Run the Streamlit application:**
    ```bash
    python -m streamlit run App.py
    ```
2.  **Access the Application:**
    Your browser should automatically open to the local address where the application is running (e.g., `http://localhost:8501`). If not, copy and paste the provided URL from your terminal into your web browser.

3.  **Interact with the UI:**
    -   Select your desired cell line from the dropdown.
    -   Enter the sgRNA sequence in the designated input field.
    -   Provide the chromosome number and select the DNA strand.
    -   The application will then process your inputs and display the predicted On-target efficacy, along with other relevant information like GC content and model confidence.



## Contact

For any questions or inquiries, please reach out to:

[Sara Aljamal] - [saraaljamal20@gmail.com]

[Sama Alqaisi] - [samaalqaisi35@gmail.com]


Project Link: [https://github.com/yourusername/project-name](https://github.com/yourusername/project-name)

