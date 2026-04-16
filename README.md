# 📧 Email Generation Assistant

### AI Engineer Candidate Assessment

An email generation assistant powered by **LLaMA models via Groq API**. Takes an intent, key facts, and a tone — generates a professional email. Includes a full automated evaluation pipeline with 3 custom metrics, a comparative analysis across 2 strategies, and a Flask web interface.

🌐 **Live Demo:** [https://email-generation-assistant-1.onrender.com](https://email-generation-assistant-1.onrender.com)

---

## 🏗️ Project Structure

email\_assistant/

├── main.py                     \# CLI runner — full evaluation or single email

├── app.py                      \# Flask web app

├── requirements.txt

├── Procfile                    \# Render deployment config

│

├── models/

│   ├── model.py                \# Groq API caller

│   ├── prompt\_builder.py       \# Strategy A (Few-Shot \+ Role-Playing) & Strategy B (Zero-Shot)

│   └── email\_generator.py      \# Connects prompt builder to model

│

├── evaluation/

│   ├── metrics.py              \# 3 custom metrics with definitions

│   └── evaluator.py            \# Normalizes and combines scores

│

├── data/

│   └── test\_cases.py           \# 10 test scenarios with human reference emails

│

└── templates/

    └── index.html              \# Flask UI template

---

## ⚙️ Setup

### 1\. Clone the repository

git clone https://github.com/your-username/email-generation-assistant.git

cd email-generation-assistant

### 2\. Install dependencies

pip install \-r requirements.txt

### 3\. Get a free Groq API key

- Go to [console.groq.com](https://console.groq.com)  
- Sign up with a Google account — **no credit card required**  
- Navigate to **API Keys** → Create a new key

### 4\. Set your API key

Create a `.env` file in the project root:

GROQ\_API\_KEY=your\_key\_here

Or set it as an environment variable:

\# Linux / Mac

export GROQ\_API\_KEY=your\_key\_here

\# Windows

set GROQ\_API\_KEY=your\_key\_here

---

## 🚀 Running the Project

### Option 1 — Full Evaluation (CLI)

Runs all 10 test cases through both strategies. Saves `results.csv`.

python main.py

\# Enter 1 when prompted

### Option 2 — Single Email (Interactive CLI)

python main.py

\# Enter 2 when prompted

### Option 3 — Web UI (Flask)

python app.py

\# Open http://localhost:5000

---

## 🤖 Models & Prompting Strategies

|  | Strategy A | Strategy B |
| :---- | :---- | :---- |
| **Model** | `llama-3.1-8b-instant` | `llama3-70b-8192` |
| **Technique** | Few-Shot \+ Role-Playing | Zero-Shot (baseline) |
| **Description** | Model given an expert role \+ 2 worked examples before the actual task | Plain instruction, no role, no examples |

**Comparison rationale:** Strategy A applies advanced prompting to a smaller, faster model. Strategy B uses a larger model with a minimal prompt. This directly tests whether prompting technique can compensate for model size — a practically important trade-off between cost, speed, and output quality.

---

## 📊 Custom Evaluation Metrics

All metrics are scored on a **1–5 scale** and averaged per email.

---

### Metric 1 — Fact Recall Score

**What it measures:** What fraction of required key facts appear in the generated email.

**Logic:**

- For each fact, extract keywords (words \> 3 characters)  
- A fact is "recalled" if ≥ 60% of its keywords appear in the email (case-insensitive)  
- Score \= `recalled / total` → normalized from 0.0–1.0 to 1–5

**Method:** Rule-based keyword matching (deterministic, no LLM call needed)

**Why it matters:** An email that drops required facts is incomplete regardless of writing quality.

---

### Metric 2 — Tone Accuracy Score

**What it measures:** How well the email's tone matches the requested tone (formal, casual, urgent, etc.)

**Logic:**

- LLM judge receives the email \+ expected tone  
- Returns a score from 1 to 5  
- 1 \= completely wrong tone, 5 \= perfectly matched

**Method:** LLM-as-a-Judge (`llama-3.1-8b-instant` via Groq)

**Why it matters:** Tone mismatch is the most immediately visible quality failure in professional emails.

---

### Metric 3 — Clarity & Structure Score

**What it measures:** How clear, well-structured, and grammatically correct the email is.

**Logic:**

- LLM judge checks: subject line, greeting, logical paragraph flow, grammar, appropriate length, closing  
- 1 \= poor structure or grammar issues, 5 \= excellent across all dimensions

**Method:** LLM-as-a-Judge (`llama-3.1-8b-instant` via Groq)

**Why it matters:** A factually complete, correctly-toned email still fails if it is confusing or poorly structured.

---

## 📈 Evaluation Results

Results from running all 10 scenarios through both strategies (`results.csv`):

| Metric | Strategy A (Few-Shot, 8B) | Strategy B (Zero-Shot, 70B) |
| :---- | :---- | :---- |
| Fact Recall (1–5) | 4.50 | **4.67** |
| Tone Accuracy (1–5) | 4.30 | **4.40** |
| Clarity & Structure (1–5) | **4.30** | 4.20 |
| **Average Score (1–5)** | 4.37 | **4.42** |

---

## 🔍 Comparative Analysis

### Which strategy performed better?

Strategy B (Zero-Shot, `llama3-70b-8192`) scored higher overall with an average of **4.42 vs 4.37**, outperforming on Fact Recall and Tone Accuracy.

### Biggest failure mode of Strategy A

**Prompt leakage** — in 7 out of 10 test cases, Strategy A's output included raw prompt text (`INPUT:`, `EXAMPLE 3:`, `OUTPUT:`) inside the generated email body. The smaller `llama-3.1-8b-instant` model failed to cleanly separate the few-shot examples from the actual task output. This is a reliability failure: even when the email content itself was good, the output was not usable as-is.

### Biggest failure mode of Strategy B

**Verbosity** — Strategy B's 70B model consistently produced emails that were longer than necessary (sometimes 3–4 paragraphs for a simple request), reducing directness and practical usability.

### Production recommendation

**Strategy B** (`llama3-70b-8192`, Zero-Shot) is recommended for production based on:

- Higher average score across all 3 metrics  
- Zero prompt leakage — outputs are clean and directly usable  
- More consistent performance across diverse tones and intents

Strategy A's approach is worth revisiting with a stronger instruction to suppress prompt formatting, or by switching to a model that handles few-shot separation more reliably. The prompting technique itself is sound — the failure was model-size-related, not conceptual.

---

## 📁 Output File

`results.csv` columns:

| Column | Description |
| :---- | :---- |
| `ID` | Test case (1–10) |
| `Strategy` | A or B |
| `Intent` | Email purpose |
| `Tone` | Requested tone |
| `Generated_Email` | Full output |
| `Fact_Recall_Raw` | 0.0–1.0 |
| `Fact_Recall_Score (1-5)` | Normalized |
| `Tone_Accuracy_Score (1-5)` | LLM judge |
| `Clarity_Structure_Score (1-5)` | LLM judge |
| `Average_Score (1-5)` | Mean of all 3 |

---

## 🧪 Test Scenarios

| \# | Intent | Tone |
| :---- | :---- | :---- |
| 1 | Follow up after job interview | Formal |
| 2 | Request medical leave | Polite |
| 3 | Apologize for missed deadline | Empathetic |
| 4 | Team meeting reminder | Formal |
| 5 | Invite team to office party | Casual |
| 6 | Thank a colleague | Warm |
| 7 | Follow up with client on proposal | Formal |
| 8 | Urgent submission reminder | Urgent |
| 9 | Complaint about damaged product | Formal |
| 10 | Recognize team for project success | Casual |

Each scenario includes a human-written reference email.

---

## 🛠️ Tech Stack

- **LLM Provider:** [Groq](https://groq.com) — free tier, no credit card needed  
- **Models:** LLaMA 3.1 8B Instant, LLaMA 3 70B  
- **Backend:** Python 3.8+, Flask, Gunicorn  
- **Deployment:** [Render](https://render.com)  
- **Libraries:** `requests`, `pandas`, `flask`, `groq`, `python-dotenv`  
- **Evaluation:** LLM-as-a-Judge \+ rule-based keyword matching

---

## 📋 Requirements

requests\>=2.31.0

pandas\>=2.0.0

flask\>=3.0.0

gunicorn

groq

python-dotenv  
