import streamlit as st

def text_input_area():
    st.subheader("Paste your text below")
    user_text = st.text_area("Text Input", key="user_text")
    if st.button("Submit for Correction"):
        st.session_state["trigger_correction"] = True
    return user_text
