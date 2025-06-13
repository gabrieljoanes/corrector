import streamlit as st

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    result = []
    last_index = 0
    shift = 0

    # Sort by start_idx to apply left-to-right
    sorted_corrections = sorted(
        [(i, c) for i, c in enumerate(corrections) if decisions.get(i) != "rejected"],
        key=lambda x: x[1]["start_idx"]
    )

    for i, corr in sorted_corrections:
        start = corr["start_idx"]
        end = corr["end_idx"]

        # Add the text before this correction
        if last_index < start:
            result.append(original_text[last_index:start])

        original = original_text[start:end]
        corrected = corr["after"]

        result.append(f"(~~{original}~~)!{corrected}!")
        last_index = end

    # Add remaining text
    result.append(original_text[last_index:])

    final_text = ''.join(result)
    st.markdown(final_text)
