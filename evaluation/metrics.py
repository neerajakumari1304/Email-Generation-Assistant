import re
import os
import time
import requests

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
JUDGE_MODEL = "llama-3.1-8b-instant"


def _call_judge(prompt):
    """Internal helper to call the LLM judge via Groq."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    time.sleep(1)
    payload = {
        "model": JUDGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": 10
    }
    time.sleep(1)
    response = requests.post(GROQ_URL, headers={"Authorization": f"Bearer {GROQ_API_KEY}"}, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def _extract_score(text, min_val=1, max_val=5, default=3):
    """
    Extract first valid integer from LLM judge response.
    Falls back to default if none found.
    """
    numbers = re.findall(r'\b([1-9][0-9]?)\b', text)
    for n in numbers:
        val = int(n)
        if min_val <= val <= max_val:
            return val
    return default


# ─────────────────────────────────────────────
# METRIC 1: Fact Recall Score (0.0 – 1.0)
# Logic: Check what fraction of key facts are
# present in the generated email using keyword
# matching. Each fact is split into meaningful
# keywords; a fact is "recalled" if at least
# 60% of its keywords appear in the email.
# ─────────────────────────────────────────────
def fact_recall_score(email, facts):
    """
    Definition: Measures how many of the required key facts
    are actually present in the generated email.

    Logic:
    - For each fact, extract keywords (words > 3 chars).
    - A fact is considered recalled if >= 60% of its
      keywords appear in the email (case-insensitive).
    - Final score = recalled_facts / total_facts (0.0 to 1.0).

    Why: An email that omits key facts is factually incomplete
    regardless of how well-written it is.
    """
    email_lower = email.lower()
    recalled = 0

    for fact in facts:
        # Extract meaningful keywords (ignore short words)
        keywords = [w.lower() for w in fact.split() if len(w) > 3]
        if not keywords:
            recalled += 1
            continue
        matched = sum(1 for kw in keywords if kw in email_lower)
        recall_ratio = matched / len(keywords)
        if recall_ratio >= 0.6:
            recalled += 1

    return round(recalled / len(facts), 2)


# ─────────────────────────────────────────────
# METRIC 2: Tone Accuracy Score (1 – 5)
# Logic: LLM-as-a-Judge evaluates how closely
# the email's tone matches the requested tone.
# Scored 1 (completely wrong tone) to 5 (perfect).
# ─────────────────────────────────────────────
def tone_accuracy_score(email, expected_tone):
    """
    Definition: Measures how accurately the email reflects
    the requested tone (e.g., formal, casual, urgent).

    Logic:
    - Send email + expected tone to an LLM judge.
    - Judge returns a score from 1 to 5.
    - Score 1 = tone completely off, 5 = tone perfectly matched.

    Why: Tone mismatch is the most visible quality failure in
    professional emails — a casual email sent to a client reads
    as unprofessional regardless of content accuracy.
    """
    prompt = f"""You are an expert email evaluator.

Task: Rate how well the tone of this email matches the expected tone.

Expected tone: {expected_tone}

Email:
{email}

Scoring guide:
5 = Tone matches perfectly throughout
4 = Mostly correct tone with minor deviations
3 = Partially correct, noticeable tone issues
2 = Wrong tone in most sections
1 = Completely wrong tone

Reply with ONLY a single digit (1 to 5). Nothing else."""

    result = _call_judge(prompt)
    return _extract_score(result, 1, 5, default=3)


# ─────────────────────────────────────────────
# METRIC 3: Clarity & Structure Score (1 – 5)
# Logic: LLM-as-a-Judge evaluates readability,
# logical flow, grammar, and email structure
# (subject line, greeting, body, closing).
# ─────────────────────────────────────────────
def clarity_structure_score(email):
    """
    Definition: Measures how clear, well-structured, and
    grammatically sound the email is.

    Logic:
    - LLM judge evaluates: subject line presence, greeting,
      logical paragraph flow, grammar, and closing.
    - Score 1 (poorly written/structured) to 5 (excellent).

    Why: A factually correct and well-toned email still fails
    if it is confusing, grammatically incorrect, or missing
    standard email components.
    """
    prompt = f"""You are an expert email evaluator.

Task: Rate this email on clarity, grammar, and structure.

Evaluate these aspects:
- Does it have a subject line?
- Does it have a proper greeting and closing?
- Is the body logically organized?
- Is the language clear and grammatically correct?
- Is the length appropriate (not too short, not too long)?

Email:
{email}

Scoring guide:
5 = Excellent structure, clear language, no grammar issues
4 = Good overall, minor issues
3 = Acceptable but noticeable problems
2 = Poor structure or multiple grammar issues
1 = Very poor, hard to understand

Reply with ONLY a single digit (1 to 5). Nothing else."""

    result = _call_judge(prompt)
    return _extract_score(result, 1, 5, default=3)
