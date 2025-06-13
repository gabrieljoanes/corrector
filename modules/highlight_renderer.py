import streamlit as st

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    if not corrections:
        st.markdown(original_text)
        return

    # Create output in segments
    result = []
    cursor = 0
    offset = 0

    # Sort by start index
    sorted_corrections = sorted(
        [(i, c) for i, c in enumerate(corrections) if decisions.get(i) != "rejected"],
        key=lambda x: x[1]["start_idx"]
    )

    for i, corr in sorted_corrections:
        start = corr["start_idx"]
        end = corr["end_idx"]

        if start < cursor or end > len(original_text):
            continue  # skip invalid or overlapping spans

        # Add unmodified text before this correction
        result.append(st.markdown(html_escape(original_text[cursor:start]), unsafe_allow_html=True))

        mistake = original_text[start:end]
        correction = corr["after"]
        label = f"[# {i + 1}]"

        before_html = f"<span style='color: red; text-decoration: line-through;'>{html_escape(mistake)}</span>"
        after_html = f"<span style='color: green; font-weight: bold;'>{html_escape(correction)}</span>"

        if i == focus_idx:
            wrapper_style = "background-color: #fff3cd; padding: 4px 6px; border-radius: 4px;"
            combined = f"<span style='{wrapper_style}'>{before_html}&nbsp;&nbsp;{after_html}&nbsp;&nbsp;<span style='font-size: 0.8em; color: gray;'>{label}</span></span>"
        else:
            combined = f"{before_html}&nbsp;&nbsp;{after_html}&nbsp;&nbsp;<span style='font-size: 0.8em; color: gray;'>{label}</span>"

        result.append(st.markdown(combined, unsafe_allow_html=True))
        cursor = end

    # Add remaining text
    result.append(st.markdown(html_escape(original_text[cursor:]), unsafe_allow_html=True))

    # Human-readable debug summary
    st.markdown("---")
    st.subheader("🛠 Debug View")
    for i, corr in enumerate(corrections):
        status = decisions.get(i, "unknown")
        st.markdown(f"""
**[#{i + 1}]**
- **Status**: `{status}`
- **Original**: `{corr["before"]}`
- **Corrected**: `{corr["after"]}`
- **Span**: `{corr["start_idx"]}–{corr["end_idx"]}`
""")

    # Machine-readable JSON block
    st.markdown("---")
    st.subheader("📦 Copy for AI Debugging")
    debug_data = [
        {
            "index": i + 1,
            "status": decisions.get(i, "unknown"),
            "before": corr["before"],
            "after": corr["after"],
            "start_idx": corr["start_idx"],
            "end_idx": corr["end_idx"]
        }
        for i, corr in enumerate(corrections)
    ]
    st.code(debug_data, language="json")


def html_escape(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\"", "&quot;")
                .replace("'", "&#x27;"))
