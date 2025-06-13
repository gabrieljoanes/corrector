import streamlit as st

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    # Build the corrected output inline
    segments = []
    cursor = 0

    sorted_corrections = sorted(
        [(i, c) for i, c in enumerate(corrections) if decisions.get(i) != "rejected"],
        key=lambda x: x[1]["start_idx"]
    )

    for i, corr in sorted_corrections:
        start = corr["start_idx"]
        end = corr["end_idx"]

        if start < cursor or end > len(original_text):
            continue

        # Unchanged text before correction
        segments.append(original_text[cursor:start])

        # Correction formatting
        mistake = original_text[start:end]
        correction = corr["after"]
        formatted = f"(~~{mistake}~~)!{correction}!"
        segments.append(formatted)

        cursor = end

    # Remaining uncorrected text
    segments.append(original_text[cursor:])

    final_text = ''.join(segments)
    st.markdown(final_text)
