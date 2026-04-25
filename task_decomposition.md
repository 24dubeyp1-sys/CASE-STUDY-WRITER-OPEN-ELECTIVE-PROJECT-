# Task Decomposition & Specifications

## **Agent 1 — Company Researcher**
- Input: Company name + business challenge
- Action: Calls Tavily Search API with targeted company/context queries
- Output: Raw research text from live web sources
- Tool Used: Tavily Search API

## **Agent 2 — Context Builder**
- Input: Raw research text from Agent 1
- Action: Sends research to Gemini Flash with a structured context prompt
- Output: Structured context summary for case study generation
- Decision Point: If research is empty or weak, returns fallback context/error note

## **Agent 3 — Case Study Writer**
- Input: Structured context from Agent 2 + original user challenge
- Action: Sends input to Gemini Flash to draft a professional case study
- Output: Full case study in markdown format
- Format: Background, Challenge, Approach, Solution, Measurable Outcomes

## **Agent 4 — LLM-as-Judge**
- Input: Full case study from Agent 3
- Action: Gemini Flash evaluates quality using a scoring rubric
- Output: JSON with scores + overall score + concise feedback
- Rubric: Factual Grounding, Narrative Flow, Structure & Clarity

## **Agent 5 — Improvement Rewriter**
- Input: Case study from Agent 3 + judge feedback from Agent 4
- Action: Uses Gemini Flash to revise weak sections and improve clarity
- Output: Improved case study draft in markdown format
- Decision Point: If overall score is below threshold, rewrite is mandatory
