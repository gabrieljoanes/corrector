def get_corrections(text):
    corrections = [
        {"before": "teh", "after": "the", "explanation": "Spelling mistake", "start_idx": text.find("teh"), "end_idx": text.find("teh") + 3}
    ]
    corrected_text = text.replace("teh", "the")
    return corrected_text, corrections
