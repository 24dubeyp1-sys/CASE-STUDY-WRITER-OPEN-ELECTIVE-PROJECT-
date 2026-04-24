import os
import json
from dotenv import load_dotenv
from agents.gemini_utils import generate_text

load_dotenv()

def judge_case_study(case_study: str, context: str) -> dict:
    """LLM-as-Judge — evaluates the case study on 3 dimensions."""
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file.")

    prompt = f"""
You are an expert evaluator for business case studies. Score the following case study on three dimensions.

REFERENCE CONTEXT (ground truth from research):
{context}

CASE STUDY TO EVALUATE:
{case_study}

Score each dimension from 1-10 and provide a brief reason. Respond ONLY in valid JSON format like this:

{{
  "factual_grounding": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "narrative_flow": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "structure": {{
    "score": <1-10>,
    "reason": "<one sentence explanation>"
  }},
  "overall_score": <average of the three, one decimal>,
  "summary": "<2-sentence overall verdict>"
}}

Scoring rubric:
- Factual Grounding: Are claims supported by the research? No hallucinations?
- Narrative Flow: Is it engaging, logical, well-paced?
- Structure: Does it follow the required format with all sections present?
"""

    raw = generate_text(prompt).strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    
    try:
        return json.loads(raw.strip())
    except json.JSONDecodeError:
        return {
            "factual_grounding": {"score": 0, "reason": "Parse error"},
            "narrative_flow": {"score": 0, "reason": "Parse error"},
            "structure": {"score": 0, "reason": "Parse error"},
            "overall_score": 0,
            "summary": "Judge output could not be parsed. Raw: " + raw[:200]
        }
