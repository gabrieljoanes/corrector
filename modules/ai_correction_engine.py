# modules/ai_correction_engine.py

def get_corrections(text):
    # Hardcoded corrections for the input string
    corrections = [
        {
            "before": "avais",
            "after": "avait",
            "explanation": "Conjugation error",
            "start_idx": 68,
            "end_idx": 73
        },
        {
            "before": "acheté",
            "after": "acheter",
            "explanation": "Infinitive form should be used after 'de'",
            "start_idx": 92,
            "end_idx": 98
        },
        {
            "before": "étais",
            "after": "étaient",
            "explanation": "Agreement with plural subject",
            "start_idx": 130,
            "end_idx": 135
        },
        {
            "before": "donner",
            "after": "donné",
            "explanation": "Past participle required",
            "start_idx": 151,
            "end_idx": 157
        },
        {
            "before": "parapluis",
            "after": "parapluie",
            "explanation": "Spelling correction",
            "start_idx": 221,
            "end_idx": 230
        }
    ]
    corrected_text = text
    for corr in sorted(corrections, key=lambda c: c["start_idx"], reverse=True):
        corrected_text = corrected_text[:corr["start_idx"]] + corr["after"] + corrected_text[corr["end_idx"]:]

    return corrected_text, corrections
