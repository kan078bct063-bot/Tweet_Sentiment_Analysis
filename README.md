# Tweet Sentiment Analysis

A machine learning project that predicts sentiment (Positive, Negative, or Neutral) from tweets using a trained LSTM neural network model.

## Overview

This project uses a deep learning model trained on the **Twitter Airline Sentiment dataset** to classify tweets into three sentiment categories. The model is deployed as an interactive web application using Streamlit.

## Features

- 🎯 **Multi-class Sentiment Classification**: Positive, Negative, and Neutral sentiments
- 🧠 **LSTM Neural Network**: Deep learning model for sequential text processing
- 🌐 **Interactive Web UI**: Easy-to-use Streamlit interface
- 📊 **Confidence Scores**: Displays prediction probabilities for each sentiment class
- 🧹 **Text Preprocessing**: Automatic tweet cleaning and normalization

## Project Structure

```
sentiment/
├── app.py                          # Streamlit application
├── sentiment_lstm_model.h5         # Trained LSTM model
├── tokenizer.pkl                   # Text tokenizer
├── label_encoder.pkl               # Sentiment label encoder
├── Sentiment_analysis_2.ipynb      # Jupyter notebook with training code
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Requirements

- Python 3.8+
- TensorFlow/Keras
- Streamlit
- NumPy
- Scikit-learn
- Pickle (built-in)

See `requirements.txt` for specific versions.

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd sentiment
```

2. **Create a virtual environment** (optional but recommended):
```bash
python -m venv sentiment_env
source sentiment_env/bin/activate  # On Windows: sentiment_env\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

### How to Use:
1. Enter a tweet or any text in the text area
2. Click the "Predict Sentiment" button
3. View the sentiment classification and confidence scores

## Model Details

- **Architecture**: LSTM (Long Short-Term Memory) Neural Network
- **Input Sequence Length**: 50 tokens
- **Output Classes**: 3 (Positive, Negative, Neutral)
- **Training Data**: Twitter Airline Sentiment Dataset

## Data Preprocessing

The model uses the following preprocessing steps:
- Converts text to lowercase
- Removes Twitter mentions (@username)
- Removes URLs
- Removes hashtags (#)
- Removes special characters
- Normalizes whitespace

This exact preprocessing is applied to user input during prediction to ensure consistency.

## Files Description

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `sentiment_lstm_model.h5` | Trained LSTM model weights |
| `tokenizer.pkl` | Tokenizer for text vectorization |
| `label_encoder.pkl` | Encoder for sentiment labels |
| `Sentiment_analysis_2.ipynb` | Jupyter notebook with model training pipeline |

## Results

The model classifies tweets into three sentiment categories:
- 😊 **Positive**: Happy, satisfied, praising sentiment
- 😐 **Neutral**: Factual, informative sentiment
- 😞 **Negative**: Unhappy, complaint, critical sentiment

Each prediction includes confidence scores for all three classes.

## Technologies Used

- **TensorFlow/Keras**: Deep learning framework
- **Streamlit**: Web application framework
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning utilities
- **Python**: Programming language

## Future Improvements

- Fine-tune model hyperparameters
- Train on larger dataset for better accuracy
- Add sentiment intensity scoring
- Support for multiple languages
- Deploy to cloud platform (Heroku, AWS, GCP)

## 🌟 Live Demo

**Try it here**: [Sentiment Analysis Demo](https://www.veed.io/view/26eba393-9afe-4c78-87a8-0a7d7057543b?source=editor&panel=share)



## License

This project is open source and available under the MIT License.

## Author

Created for Twitter Airline Sentiment Analysis Project

---

**Note**: This model is trained specifically on airline-related tweets. Performance may vary on other domains.

