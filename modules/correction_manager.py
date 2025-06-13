import streamlit as st

def initialize_state():
    for key in ["corrected_text", "corrections", "decisions", "trigger_correction", "preview_mode"]:
        if key not in st.session_state:
            st.session_state[key] = None

def detect_manual_edits(current_text):
    pass  # To be implemented

def update_decision(index, decision):
    st.session_state["decisions"][index] = decision

def get_preview_corrections():
    return [i for i, d in st.session_state["decisions"].items() if d == "accepted"]

def finalize_corrections():
    for i in st.session_state["decisions"]:
        if st.session_state["decisions"][i] == "pending":
            st.session_state["decisions"][i] = "rejected"
