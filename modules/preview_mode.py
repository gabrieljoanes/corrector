import streamlit as st
from modules.correction_manager import get_preview_corrections

def show_preview_mode():
    st.subheader("Preview Accepted Corrections")
    for i in get_preview_corrections():
        st.write(f"✔️ {st.session_state['corrections'][i]['before']} → {st.session_state['corrections'][i]['after']}")
