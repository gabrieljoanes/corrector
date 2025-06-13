import streamlit as st

def show_corrections_sidebar():
    st.sidebar.subheader("Corrections List")
    for i, corr in enumerate(st.session_state["corrections"]):
        status = st.session_state["decisions"][i]
        with st.sidebar.expander(f"Correction #{i + 1} [{status}]"):
            st.write(corr["explanation"])
            if st.button(f"Accept #{i+1}"):
                st.session_state["decisions"][i] = "accepted"
            if st.button(f"Reject #{i+1}"):
                st.session_state["decisions"][i] = "rejected"
