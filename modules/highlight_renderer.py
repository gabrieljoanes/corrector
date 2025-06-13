import streamlit as st
import re

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    sorted_corrections = sorted(
        [(i, c) for i, c in enumerate(corrections) if decisions.get(i) != "rejected"],
        key=lambda x: x[1]["start_idx"],
        reverse=True
    )

    text = original_text

    for i, corr in sorted_corrections:
        start = corr["start_idx"]
        end = corr["end_idx"]
        if start < 0 or end > len(text):
            continue

        mistake = text[start:end]
        correction = corr["after"]

        label = f"<span style='font-size: 0.8em; color: gray;'>[# {i+1}]</span>"

        before_html = f"<span style='color: red; text-decoration: line-through;'>{mistake}</span>"
        after_html = f"<span style='color: green; font-weight: bold;'>{correction}</span>"

        if i == focus_idx:
            wrapper_style = "background-color: #fff3cd; padding: 4px 6px; border-radius: 4px;"
            replacement = f"<span style='{wrapper_style}'>{before_html}&nbsp;&nbsp;{after_html}&nbsp;&nbsp;{label}</span>"
        else:
            replacement = f"{before_html}&nbsp;&nbsp;{after_html}&nbsp;&nbsp;{label}"

        replacement = f" {replacement} "
        text = text[:start] + replacement + text[end:]

    st.markdown(text, unsafe_allow_html=True)
