import streamlit as st

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    result = []
    cursor = 0
    working_text = original_text

    for i, corr in enumerate(corrections):
        if decisions.get(i) == "rejected":
            continue

        before = corr["before"]
        after = corr["after"]
        idx = working_text.find(before, cursor)

        if idx == -1:
            continue  # skip if not found

        end = idx + len(before)

        # Append untouched text
        result.append(working_text[cursor:idx])

        # Append corrected version
        result.append(f"(~~{before}~~)!{after}!")

        cursor = end

    result.append(working_text[cursor:])

    final_text = ''.join(result)
    st.markdown(final_text)
