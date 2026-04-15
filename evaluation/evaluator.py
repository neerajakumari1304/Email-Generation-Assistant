from evaluation.metrics import fact_recall_score, tone_accuracy_score, clarity_structure_score


def evaluate_email(email, facts, tone):
    """
    Run all 3 custom metrics on a generated email.

    Score normalization:
    - fact_recall: 0.0–1.0 → multiply by 5 to get 1–5 scale
    - tone_accuracy: already 1–5
    - clarity_structure: already 1–5

    Average score = mean of all three on 1–5 scale.
    """
    fact_raw = fact_recall_score(email, facts)
    fact_normalized = round(fact_raw * 5, 2)  # normalize to 1–5

    tone = tone_accuracy_score(email, tone)
    clarity = clarity_structure_score(email)

    average = round((fact_normalized + tone + clarity) / 3, 2)

    return {
        "fact_recall_raw": fact_raw,           # 0.0–1.0
        "fact_recall_score": fact_normalized,  # normalized to 1–5
        "tone_accuracy_score": tone,           # 1–5
        "clarity_structure_score": clarity,    # 1–5
        "average_score": average               # 1–5
    }
