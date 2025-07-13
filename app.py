import streamlit as st
import joblib

# Load models
category_model = joblib.load("bug_model.pkl")
category_vectorizer = joblib.load("vectorizer.pkl")
priority_model = joblib.load("bug_priority_model.pkl")
priority_vectorizer = joblib.load("vectorizer_priority.pkl")


st.set_page_config(page_title="BugTrack AI", layout="centered")
st.title("🐞 BugTrack AI – Smart Bug & Priority Classifier")
st.markdown("Predicts the **Category** and **Priority** of any bug report using AI 🔮")

bug_title = st.text_input("📝 Bug Title", placeholder="e.g., Crash on login")
bug_description = st.text_area("🧾 Bug Description", placeholder="e.g., App crashes when user logs in")

if st.button("🔍 Predict"):
    if bug_title.strip() and bug_description.strip():
        # Predict category
        input_cat = category_vectorizer.transform([bug_description])
        category = category_model.predict(input_cat)[0]

        # Predict priority
        full_text = bug_title + " " + bug_description
        input_priority = priority_vectorizer.transform([full_text])
        priority = priority_model.predict(input_priority)[0]

        st.success(f"🧠 Predicted Category: `{category}`")
        st.info(f"⚡ Predicted Priority: `{priority}`")
    else:
        st.warning("⚠️ Please enter both Title and Description.")
