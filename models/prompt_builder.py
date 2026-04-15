def build_advanced_prompt(intent, facts, tone):
    """
    Strategy A: Role-Playing + Few-Shot prompting.
    The model is assigned a role and given 2 examples
    before seeing the actual task. This is the advanced technique.
    """

    facts_text = "\n".join(f"- {f}" for f in facts)

    # Few-shot example 1
    example_1 = """
INPUT:
Intent: Follow up after a job interview
Facts:
- Interviewed on Tuesday for Data Analyst role
- Interviewer was Ms. Priya
- Keen to know next steps
Tone: formal

OUTPUT:
Subject: Follow-Up on Data Analyst Interview – Tuesday

Dear Ms. Priya,

Thank you for taking the time to meet with me on Tuesday for the Data Analyst position. I truly enjoyed our conversation and learning more about the team's goals.

I remain very interested in the role and would love to contribute to your organization. Could you kindly share any updates regarding the next steps in the hiring process?

I appreciate your time and look forward to hearing from you.

Warm regards,
[Candidate Name]
"""

    # Few-shot example 2
    example_2 = """
INPUT:
Intent: Apologize for missing a deadline
Facts:
- Deadline missed by 1 day
- Reason was power outage at home
- Will deliver by evening today
Tone: empathetic

OUTPUT:
Subject: Sincere Apology for Delayed Submission

Dear [Manager Name],

I sincerely apologize for missing yesterday's deadline. I fully understand the pressure this may have caused and take complete responsibility.

The delay was caused by an unexpected power outage at my home, which disrupted my ability to finalize the work. I want to assure you that the deliverable will be in your inbox by this evening.

Thank you for your patience and understanding. I will ensure this does not happen again.

Best regards,
[Your Name]
"""

    prompt = f"""You are an expert professional email writer with 15 years of experience crafting emails for corporate, client-facing, and internal communication. You write emails that are natural, human, and highly effective.

Here are two examples of how you write emails:

EXAMPLE 1:
{example_1}

EXAMPLE 2:
{example_2}

Now write a new email using the same quality and structure.

INPUT:
Intent: {intent}
Facts:
{facts_text}
Tone: {tone}

OUTPUT:
"""
    return prompt


def build_basic_prompt(intent, facts, tone):
    """
    Strategy B: Zero-Shot basic prompt.
    No role, no examples. Plain instruction only.
    Used for comparison against Strategy A.
    """

    facts_text = "\n".join(f"- {f}" for f in facts)

    prompt = f"""Write a {tone} professional email.

Intent: {intent}

Key Facts to include:
{facts_text}

Write the email now:
"""
    return prompt
