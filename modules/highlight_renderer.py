import streamlit as st
import streamlit.components.v1 as components
import string

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    result = []
    cursor = 0
    text = original_text
    final_output = ""

    for i, corr in enumerate(corrections):
        if decisions.get(i) == "rejected":
            continue

        before = corr["before"]
        after = corr["after"]

        # Find match with boundary-aware logic
        search_pos = cursor
        while True:
            idx = text.find(before, search_pos)
            if idx == -1:
                break

            pre = text[idx - 1] if idx > 0 else " "
            post = text[idx + len(before)] if idx + len(before) < len(text) else " "

            if pre in string.whitespace + string.punctuation and post in string.whitespace + string.punctuation:
                break
            else:
                search_pos = idx + 1

        if idx == -1:
            continue

        result.append(text[cursor:idx])
        result.append(f"(~~{before}~~)!{after}!")
        cursor = idx + len(before)

    result.append(text[cursor:])
    final_output = ''.join(result)

    # Show final output
    st.markdown(final_output)

    # Add copy button
    components.html(f"""
        <textarea id='outputText' style='width:100%; height:150px;'>{final_output}</textarea>
        <button onclick="navigator.clipboard.writeText(document.getElementById('outputText').value)">📋 Copy Output</button>
    """, height=200)
