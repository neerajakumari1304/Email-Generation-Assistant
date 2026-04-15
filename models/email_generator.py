from models.model import call_model
from models.prompt_builder import build_advanced_prompt, build_basic_prompt

# Model A: smaller/faster llama model with advanced prompting
MODEL_A_NAME = "llama-3.1-8b-instant"

# Model B: larger llama model with basic prompting
MODEL_B_NAME = "llama-3.3-70b-versatile"


def generate_email_strategy_a(intent, facts, tone):
    """
    Strategy A: llama-3.1-8b-instant + Role-Playing + Few-Shot prompt.
    Advanced prompting technique applied.
    """
    prompt = build_advanced_prompt(intent, facts, tone)
    return call_model(prompt, model_name=MODEL_A_NAME)


def generate_email_strategy_b(intent, facts, tone):
    """
    Strategy B: llama3-70b-8192 + Zero-Shot basic prompt.
    No examples, no role. Baseline comparison.
    """
    prompt = build_basic_prompt(intent, facts, tone)
    return call_model(prompt, model_name=MODEL_B_NAME)
