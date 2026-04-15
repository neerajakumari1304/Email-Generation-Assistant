import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import time

import pandas as pd
from models.email_generator import generate_email_strategy_a, generate_email_strategy_b
from evaluation.evaluator import evaluate_email
from data.test_cases import test_cases


def run_evaluation():
    """
    Run all 10 test cases through both strategies.
    Save results to results.csv with scores for all 3 metrics.
    """
    results = []

    for case in test_cases:
        i = case["id"]
        intent = case["intent"]
        facts = case["facts"]
        tone = case["tone"]

        print(f"\n{'='*60}")
        print(f"Test Case {i}: {intent} | Tone: {tone}")
        print(f"{'='*60}")

        # --- Strategy A ---
        print(f"\n[Strategy A] llama-3.1-8b-instant + Few-Shot + Role-Playing")
        email_a = generate_email_strategy_a(intent, facts, tone)
        time.sleep(2)
        print(email_a[:300] + "..." if len(email_a) > 300 else email_a)
        scores_a = evaluate_email(email_a, facts, tone)
        time.sleep(2)
        print(f"Scores A: {scores_a}")

        results.append({
            "ID": i,
            "Strategy": "A - Few-Shot + Role-Playing (llama-3.1-8b-instant)",
            "Intent": intent,
            "Tone": tone,
            "Generated_Email": email_a.replace("\n", " "),
            "Fact_Recall_Raw": scores_a["fact_recall_raw"],
            "Fact_Recall_Score (1-5)": scores_a["fact_recall_score"],
            "Tone_Accuracy_Score (1-5)": scores_a["tone_accuracy_score"],
            "Clarity_Structure_Score (1-5)": scores_a["clarity_structure_score"],
            "Average_Score (1-5)": scores_a["average_score"]
        })

        # --- Strategy B ---
        print(f"\n[Strategy B] llama3-70b-8192 + Zero-Shot basic prompt")
        email_b = generate_email_strategy_b(intent, facts, tone)
        time.sleep(2)
        print(email_b[:300] + "..." if len(email_b) > 300 else email_b)
        scores_b = evaluate_email(email_b, facts, tone)
        time.sleep(2)
        print(f"Scores B: {scores_b}")

        results.append({
            "ID": i,
            "Strategy": "B - Zero-Shot (llama3-70b-8192)",
            "Intent": intent,
            "Tone": tone,
            "Generated_Email": email_b.replace("\n", " "),
            "Fact_Recall_Raw": scores_b["fact_recall_raw"],
            "Fact_Recall_Score (1-5)": scores_b["fact_recall_score"],
            "Tone_Accuracy_Score (1-5)": scores_b["tone_accuracy_score"],
            "Clarity_Structure_Score (1-5)": scores_b["clarity_structure_score"],
            "Average_Score (1-5)": scores_b["average_score"]
        })

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)
    print("\n\nResults saved to results.csv")

    # Print summary
    print("\n" + "="*60)
    print("AVERAGE SCORES BY STRATEGY")
    print("="*60)
    summary = df.groupby("Strategy")[
        ["Fact_Recall_Score (1-5)", "Tone_Accuracy_Score (1-5)",
         "Clarity_Structure_Score (1-5)", "Average_Score (1-5)"]
    ].mean().round(2)
    print(summary.to_string())

    return df


def run_user_input():
    """Interactive mode: user enters intent, facts, tone."""
    print("\n--- User Input Mode ---")
    intent = input("Enter intent (e.g. Follow up after interview): ").strip()
    facts_raw = input("Enter facts separated by commas: ").strip()
    facts = [f.strip() for f in facts_raw.split(",")]
    tone = input("Enter tone (formal/casual/urgent/polite/empathetic): ").strip()

    print("\nChoose strategy:")
    print("1. Strategy A — Few-Shot + Role-Playing (llama-3.1-8b-instant)")
    print("2. Strategy B — Zero-Shot (llama3-70b-8192)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        email = generate_email_strategy_a(intent, facts, tone)
    else:
        email = generate_email_strategy_b(intent, facts, tone)

    print("\n--- Generated Email ---\n")
    print(email)

    scores = evaluate_email(email, facts, tone)
    print("\n--- Evaluation Scores ---")
    for k, v in scores.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    print("Choose Mode:")
    print("1. Run full evaluation (10 test cases × 2 strategies → results.csv)")
    print("2. User Input Mode (generate a single email)")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "1":
        run_evaluation()
    elif choice == "2":
        run_user_input()
    else:
        print("Invalid choice.")
