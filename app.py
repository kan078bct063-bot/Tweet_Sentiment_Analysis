import streamlit as st
import pickle
import numpy as np
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and files
model = load_model('sentiment_lstm_model.h5', compile=False)

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# EXACT same cleaning function used during training
def clean_tweet(text):
    text = text.lower()
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'#(\w+)', r'\1', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

st.title("✈️ Tweet Sentiment Analysis")
st.write("Trained on Twitter Airline Sentiment dataset")

user_input = st.text_area("Enter a tweet here:")

if st.button("Predict Sentiment"):
    if user_input.strip():
        # Clean exactly like training data
        cleaned = clean_tweet(user_input)

        # Tokenize and pad — maxlen=50 matches training!
        sequence = tokenizer.texts_to_sequences([cleaned])
        padded = pad_sequences(sequence, maxlen=50, padding='post', truncating='post')

        # Predict
        pred = model.predict(padded, verbose=0)

        neg_prob = float(pred[0][0])
        neu_prob = float(pred[0][1])
        pos_prob = float(pred[0][2])

        predicted_label = label_encoder.inverse_transform([pred.argmax()])[0]

        # Display result
        if predicted_label == 'positive':
            st.success(f"😊 Sentiment: **Positive**")
        elif predicted_label == 'negative':
            st.error(f"😞 Sentiment: **Negative**")
        else:
            st.info(f"😐 Sentiment: **Neutral**")

        # Show probabilities
        st.write("### Confidence Scores:")
        st.progress(pos_prob, text=f"Positive: {pos_prob:.2%}")
        st.progress(neu_prob, text=f"Neutral:  {neu_prob:.2%}")
        st.progress(neg_prob, text=f"Negative: {neg_prob:.2%}")

    else:
        st.warning("Please enter some text")