
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_corrections(text):
    prompt = f"""
You are an expert proofreader. Review the following text and return a list of spelling or grammar corrections.
For each correction, give:
- the original (incorrect) text
- the corrected text
- a short explanation
- the character start and end positions of the incorrect text in the original input.

Return ONLY a valid JSON list with the following format:
[
  {{
    "before": "...",
    "after": "...",
    "explanation": "...",
    "start_idx": ...,
    "end_idx": ...
  }},
  ...
]

Input text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        corrections = eval(content)
    except Exception:
        corrections = []

    corrected_text = text
    for corr in sorted(corrections, key=lambda c: c["start_idx"], reverse=True):
        corrected_text = (
            corrected_text[:corr["start_idx"]] +
            corr["after"] +
            corrected_text[corr["end_idx"]:]
        )

    return corrected_text, corrections
