# ✍️ Case Study Writer Agent

A multi-agent AI system that automatically researches a company,
builds business context, writes a professional case study, and scores
its quality using an LLM-as-Judge.

Click one button — all agents run sequentially and generate a
structured case study with evaluation scores in under 60 seconds.

---

## 🚀 Live Demo

App runs locally using Streamlit.
To run it yourself, follow the steps in the Run Locally section below.

---

## 🎯 Problem Statement

Writing strong business case studies usually takes hours of manual
research, structure planning, and editing. Founders, analysts, and
students often struggle to turn scattered company information into a
clear narrative.

This system reduces that process to under 60 seconds using Agentic AI.

**Users:** Product managers, consultants, startup teams, students

---

## 🤖 How It Works

4 AI stages run in sequence automatically:

1. 🔍 **Researcher** — fetches raw company and industry data via Tavily
2. 🧠 **Context Builder** — converts raw results into structured context
3. ✍️ **Writer** — drafts a full markdown case study
4. ⚖️ **LLM-as-Judge** — evaluates quality across 3 dimensions

Each agent passes output to the next automatically.
No manual intervention is needed between steps.

---

## 📊 What The Output Includes

- Structured case study in markdown format
- Core business challenge framing
- Situation-context-analysis narrative flow
- LLM Judge scores:
  - Factual Accuracy
  - Narrative Quality
  - Structure & Clarity
  - Overall Score

---

## 🏗️ Case Study Writer Agent — Architecture

```
User Input
Company Name + Business Challenge
        │
        ▼
Streamlit UI
app.py · orchestrates all agents
        │
        ▼
Sequential Pipeline
        │
        ├── Agent 1: Researcher
        │   researcher.py · fetches raw data
        │   External API: Tavily Search
        │   Web search · 4 results per query
        │   Output: raw results dict
        │
        ├── Agent 2: Context Builder
        │   context_builder.py · structures research
        │   LLM: Gemini Flash
        │   Output: structured context str
        │
        ├── Agent 3: Writer
        │   writer.py · drafts case study
        │   LLM: Gemini Flash
        │   Output: markdown case study str
        │
        └── LLM-as-Judge
            judge.py · evaluates on 3 dimensions
            LLM: Gemini Flash
            Output: JSON verdict
        │
        ▼
Streamlit Output
Case study + Scores
(Factual · Narrative · Structure · Overall)
```

### Shared Utility

`gemini_utils.py`

- `generate_text()`
- Auto model fallback:
  - `gemini-2.0-flash`
  - `gemini-2.0-flash-lite`
  - `gemini-1.5-flash-latest`
  - Dynamic model discovery fallback

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web UI framework |
| Gemini API (Flash models) | LLM engine for context, writing, and judging |
| Tavily Search API | Live internet research |
| python-dotenv | Secure API key management |

---

## ⚙️ Run Locally

**Step 1 — Clone the repo**

```bash
git clone <your-repo-url>
cd case-study-agent
```

**Step 2 — Create virtual environment**

```bash
python -m venv .venv
```

**Step 3 — Activate environment**

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Mac/Linux:

```bash
source .venv/bin/activate
```

**Step 4 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 5 — Add API keys**

Create a `.env` file in project root:

```env
GEMINI_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
```

**Step 6 — Run app**

```bash
streamlit run app.py
```

---

## 🔑 API Keys

- Gemini API key: [Google AI Studio](https://aistudio.google.com/app/apikey)
- Tavily API key: [Tavily](https://tavily.com)
