import os
from dotenv import load_dotenv
from agents.gemini_utils import generate_text

load_dotenv()

def write_case_study(company_name: str, challenge: str, context: str) -> str:
    """Agent 3: Case Study Writer — produces the final structured case study."""
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file.")

    prompt = f"""
You are a professional business case study writer. Using the structured context below, write a complete, engaging case study about {company_name} and the challenge: "{challenge}".

CONTEXT:
{context}

Write the case study in this exact structure:

# {company_name}: [Create a compelling subtitle]

## Executive Summary
[2-3 sentence overview of the challenge and outcome]

## Company Background
[Who they are, what they do, their market position]

## The Challenge
[The specific business problem, its scale, and why it was urgent]

## Approach & Solution
[How they addressed the challenge — strategy, tools, teams, decisions]

## Results & Impact
[Measurable outcomes, business impact, lessons learned]

## Key Takeaways
[3 bullet points: what others can learn from this case]

Write in a professional but engaging tone. Be specific. Use numbers where available.
"""

    return generate_text(prompt)
