import streamlit as st
from agents.researcher import research_company
from agents.context_builder import build_context
from agents.writer import write_case_study
from agents.judge import judge_case_study

st.set_page_config(
    page_title="Case Study Writer Agent",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Case Study Writer Agent")
st.caption("AI-powered case study generation with research, writing, and evaluation.")

st.divider()
col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input("🏢 Company Name", placeholder="e.g. Netflix, Zomato, Infosys")

with col2:
    challenge = st.text_input("⚡ Business Challenge", placeholder="e.g. content localization at scale")

run = st.button("🚀 Generate Case Study", use_container_width=True, type="primary")

if run:
    if not company_name or not challenge:
        st.warning("Please fill in both fields.")
        st.stop()

    try:
        with st.status("🔍 Agent 1: Researching company and challenge via Tavily...", expanded=True) as status:
            research = research_company(company_name, challenge)

            with st.expander("📰 Raw Research Results"):
                st.write("**Company Data:**")
                for r in research.get("company_data", []):
                    title = r.get("title", "Untitled source") if isinstance(r, dict) else "Untitled source"
                    url = r.get("url", "") if isinstance(r, dict) else ""
                    st.markdown(f"- [{title}]({url})" if url else f"- {title}")
                st.write("**Challenge Data:**")
                for r in research.get("challenge_data", []):
                    title = r.get("title", "Untitled source") if isinstance(r, dict) else "Untitled source"
                    url = r.get("url", "") if isinstance(r, dict) else ""
                    st.markdown(f"- [{title}]({url})" if url else f"- {title}")

            status.update(label="✅ Research complete", state="complete")

        with st.status("🧠 Agent 2: Building structured context...", expanded=False) as status:
            context = build_context(company_name, challenge, research)

            with st.expander("🗂️ Structured Context"):
                st.markdown(context)

            status.update(label="✅ Context built", state="complete")

        with st.status("✍️ Agent 3: Writing case study...", expanded=False) as status:
            case_study = write_case_study(company_name, challenge, context)
            status.update(label="✅ Case study written", state="complete")

        with st.status("⚖️ LLM-as-Judge: Evaluating output quality...", expanded=False) as status:
            verdict = judge_case_study(case_study, context)
            status.update(label="✅ Evaluation complete", state="complete")
    except Exception as exc:
        st.error(f"Generation failed: {exc}")
        st.stop()

    st.divider()
    st.subheader("📄 Generated Case Study")
    st.markdown(case_study)

    st.download_button(
        label="⬇️ Download as .txt",
        data=case_study,
        file_name=f"{company_name.replace(' ', '_')}_case_study.txt",
        mime="text/plain"
    )

    st.divider()
    st.subheader("⚖️ LLM-as-Judge Evaluation")

    c1, c2, c3, c4 = st.columns(4)
    factual_grounding = verdict.get("factual_grounding", {})
    narrative_flow = verdict.get("narrative_flow", {})
    structure = verdict.get("structure", {})

    c1.metric("Factual Grounding", f"{factual_grounding.get('score', 0)}/10")
    c2.metric("Narrative Flow", f"{narrative_flow.get('score', 0)}/10")
    c3.metric("Structure", f"{structure.get('score', 0)}/10")
    c4.metric("Overall Score", f"{verdict.get('overall_score', 0)}/10")

    st.info(f"**Verdict:** {verdict.get('summary', 'No summary returned by judge.')}")

    with st.expander("📊 Detailed Scoring Breakdown"):
        for dim, payload in [
            ("factual_grounding", factual_grounding),
            ("narrative_flow", narrative_flow),
            ("structure", structure),
        ]:
            st.markdown(
                f"**{dim.replace('_', ' ').title()}** — {payload.get('reason', 'No reason returned.')}"
            )
