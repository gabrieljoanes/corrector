import streamlit as st

def render_highlighted_text(original_text, corrections, decisions, focus_idx=None):
    st.subheader("Corrected Text")

    # Prepare inline replacements
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
            continue  # overlapping or invalid span

        # Add plain text before correction
        segments.append(original_text[cursor:start])

        # Add formatted correction
        mistake = original_text[start:end]
        corrected = corr["after"]
        label = f"[#{i+1}]"

        inline = f"~~{mistake}~~ **{corrected}** {label}"
        segments.append(inline)

        cursor = end

    # Add remaining text
    segments.append(original_text[cursor:])

    # Final assembled output
    final_text = ''.join(segments)
    st.markdown(final_text)

    # --- DEBUG: readable summary
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

    # --- DEBUG: machine-readable output
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
