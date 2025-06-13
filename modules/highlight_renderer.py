import streamlit as st

def render_highlighted_text(text, corrections, decisions, focus_idx):
    st.subheader("Corrected Text")
    for i, corr in enumerate(corrections):
        if decisions[i] != "rejected":
            text = text.replace(corr["after"], f"**{corr['after']}**")
    st.markdown(text)
