import streamlit as st
import joblib
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_model = os.path.join(script_dir, "model_lg.joblib")
file_path_vector = os.path.join(script_dir, "ai_human_vec.joblib")

model = joblib.load(file_path_model)
vectorizer = joblib.load(file_path_vector)

st.set_page_config(page_title="TextGuard - AI vs Human Text Detector", page_icon="🛡️")

st.markdown("<h1 style='text-align: center;'>TextGuard</h1>", unsafe_allow_html=True)
st.subheader("AI vs Human Text Detector")

user_input = st.text_area("Enter text to analyze:", height=200)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vector_text = vectorizer.transform([user_input])
        prediction = model.predict(vector_text)[0]

        if prediction == 1:
            st.error("This text is AI Generated")
        else:
            st.success("This text is Human Generated")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Hamza</p>", unsafe_allow_html=True)
