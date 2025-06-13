import streamlit as st
from modules.text_input_module import text_input_area
from modules.ai_correction_engine import get_corrections
from modules.highlight_renderer import render_highlighted_text
from modules.correction_sidebar import show_corrections_sidebar
from modules.correction_manager import (
    initialize_state, update_decision, get_preview_corrections,
    finalize_corrections, detect_manual_edits
)
from modules.preview_mode import show_preview_mode
from modules.final_submit_module import handle_final_submission

st.set_page_config(page_title="AI Text Correction Tool", layout="wide")

initialize_state()
st.title("Interactive AI Text Correction")

user_input = text_input_area()
if st.session_state.get("trigger_correction"):
    corrected_text, corrections = get_corrections(user_input)
    st.session_state["corrected_text"] = corrected_text
    st.session_state["corrections"] = corrections
    st.session_state["decisions"] = {i: "pending" for i in range(len(corrections))}

if st.session_state.get("corrected_text"):
    detect_manual_edits(user_input)
    render_highlighted_text(
        st.session_state["corrected_text"],
        st.session_state["corrections"],
        st.session_state["decisions"],
        st.session_state.get("highlight_focus")
    )
    show_corrections_sidebar()

if st.session_state.get("preview_mode"):
    show_preview_mode()

handle_final_submission()
