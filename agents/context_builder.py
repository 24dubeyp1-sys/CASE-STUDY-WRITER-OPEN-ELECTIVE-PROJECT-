import os
from dotenv import load_dotenv
from agents.gemini_utils import generate_text

load_dotenv()

def build_context(company_name: str, challenge: str, research: dict) -> str:
    """Agent 2: Context Builder — synthesizes raw research into structured context."""

    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("Missing GEMINI_API_KEY. Add it to your .env file.")

    company_snippets = "\n".join(
        [
            f"- {r.get('title', 'Untitled source')}: {str(r.get('content', ''))[:300]}"
            for r in research.get("company_data", [])
            if isinstance(r, dict)
        ]
    )
    challenge_snippets = "\n".join(
        [
            f"- {r.get('title', 'Untitled source')}: {str(r.get('content', ''))[:300]}"
            for r in research.get("challenge_data", [])
            if isinstance(r, dict)
        ]
    )

    prompt = f"""
You are a business analyst. Based on the research below, extract and organize key facts about {company_name} and the challenge: "{challenge}".

COMPANY RESEARCH:
{company_snippets}

CHALLENGE RESEARCH:
{challenge_snippets}

Produce a structured context summary with these sections:
1. Company Background (industry, size, founding, core business)
2. The Business Challenge (what problem they faced, why it mattered)
3. Approach Taken (how they tackled it, teams/tools involved)
4. Key Outcomes (measurable results if available)

Be factual. Only use information from the research above. Flag anything uncertain.
"""

    return generate_text(prompt)
