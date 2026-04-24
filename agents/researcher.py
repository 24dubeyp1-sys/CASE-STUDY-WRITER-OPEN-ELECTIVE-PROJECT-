from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

def research_company(company_name: str, challenge: str) -> dict:
    """Agent 1: Company Researcher — fetches raw data via Tavily."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Missing TAVILY_API_KEY. Add it to your .env file.")

    client = TavilyClient(api_key=api_key)

    company_results = client.search(
        query=f"{company_name} company overview business model history",
        max_results=4,
        search_depth="advanced"
    )

    challenge_results = client.search(
        query=f"{company_name} {challenge} strategy solution outcome",
        max_results=4,
        search_depth="advanced"
    )

    return {
        "company_data": company_results.get("results", []) if isinstance(company_results, dict) else [],
        "challenge_data": challenge_results.get("results", []) if isinstance(challenge_results, dict) else []
    }
