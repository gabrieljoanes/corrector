import streamlit as st
import re

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    result = []
    cursor = 0
    working_text = original_text
    used_spans = set()

    for i, corr in enumerate(corrections):
        if decisions.get(i) == "rejected":
            continue

        before = corr["before"]
        after = corr["after"]

        # Match whole word only
        pattern = r'\b{}\b'.format(re.escape(before))
        match = re.search(pattern, working_text[cursor:])

        if not match:
            continue

        span_start = cursor + match.start()
        span_end = cursor + match.end()

        # Add text before match
        result.append(working_text[cursor:span_start])

        # Add formatted correction
        result.append(f"(~~{before}~~)!{after}!")

        cursor = span_end

    result.append(working_text[cursor:])

    final_text = ''.join(result)
    st.markdown(final_text)
