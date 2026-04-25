# Problem Statement

## Project Name
Case Study Writer Agent

## The Problem
Given a company name and a business challenge, creating a strong case
study still takes significant manual work. Teams must search multiple
sources, understand business context, structure the story, and draft
clear outcomes.

This process is time-consuming, inconsistent, and hard to scale across
projects.

## User
Consultants, product managers, startup teams, analysts, and students
who need professional case studies quickly.

## Need
An automated system that instantly generates a structured case study
from minimal input — company name + business challenge — including:
- company background
- challenge context
- approach and solution
- measurable outcomes

The system must also score quality so users can assess trust and
readiness before sharing the draft.

## Why Agentic
This problem requires multiple sequential reasoning steps:
- Searching live internet data (Tavily)
- Building structured context from research (Context Builder)
- Writing a professional case study (Case Study Writer)
- Evaluating output quality (LLM-as-Judge)

No single AI call can perform all these steps reliably. Each step
depends on the output of the previous one. Only an agentic architecture
where agents run autonomously and sequentially can solve this end-to-end.

## Agent Pipeline
- Company Researcher
- Context Builder
- Case Study Writer
- LLM-as-Judge

## External Tool
- Tavily Search API
