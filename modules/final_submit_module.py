import streamlit as st
import json
from modules.correction_manager import finalize_corrections

def handle_final_submission():
    if st.button("Submit Final Version"):
        finalize_corrections()
        output_text = st.session_state["corrected_text"]
        data = {
            "input": st.session_state["user_text"],
            "output": output_text,
            "corrections": [
                {
                    "before": c["before"],
                    "after": c["after"],
                    "explanation": c["explanation"],
                    "status": st.session_state["decisions"][i]
                } for i, c in enumerate(st.session_state["corrections"])
            ]
        }
        with open("fewshots.json", "w") as f:
            json.dump(data, f, indent=2)
        st.success("Final text and JSON file generated.")
