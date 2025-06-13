import streamlit as st
import html

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    # Sort corrections by start index descending to not affect following ranges
    valid_corrections = [
        (i, c) for i, c in enumerate(corrections)
        if decisions.get(i) != "rejected" and c["start_idx"] != -1
    ]
    sorted_corrections = sorted(valid_corrections, key=lambda x: x[1]["start_idx"], reverse=True)

    text = html.escape(original_text)

    for i, corr in sorted_corrections:
        start = corr["start_idx"]
        end = corr["end_idx"]

        before = text[start:end]
        after = html.escape(corr["after"])

        style = (
            "background-color: #ff7043; padding: 2px 4px; border-radius: 4px;"
            if i == focus_idx else
            "background-color: #fff176; padding: 2px 4px; border-radius: 4px;"
        )

        highlighted = f"<span style='{style}' title='Correction #{i+1}'>{after}</span>"
        text = text[:start] + highlighted + text[end:]

    st.markdown(text, unsafe_allow_html=True)
