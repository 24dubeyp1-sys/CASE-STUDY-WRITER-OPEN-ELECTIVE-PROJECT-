# Case Study Writer Agent

An AI agent pipeline that researches a company, builds context, writes a case study, and evaluates it using an LLM-as-Judge.

## Architecture

```
User Input (Company + Challenge)
        │
        ▼
┌─────────────────┐
│  Streamlit UI   │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ Agent 1: Researcher │◄──── Tavily Search API
└────────┬────────────┘
         │
         ▼
┌──────────────────────────┐
│ Agent 2: Context Builder │◄──── Gemini 1.5 Flash
└────────┬─────────────────┘
         │
         ▼
┌─────────────────────┐
│ Agent 3: Writer     │◄──── Gemini 1.5 Flash
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ LLM-as-Judge        │◄──── Gemini 1.5 Flash
└────────┬────────────┘
         │
         ▼
  Output + Scores on UI
```

## Setup

1. Clone the repo
2. Create `.env` from `.env.example` and add your API keys
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## API Keys

- Gemini: https://aistudio.google.com/app/apikey (free)
- Tavily: https://tavily.com (free tier)
