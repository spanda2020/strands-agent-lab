from strands import Agent

from strands_agent_lab.models.local_models import get_qwen_4b
from strands_agent_lab.tools.ads_tools import get_campaign_metrics


ADS_ANALYST_INSTRUCTIONS = """
You are an expert Advertising Data Analyst.
Your objective is to analyze advertising campaign performance.

CORE OPERATIONAL RULES:

1. Identify the metrics relevant to the user's question.
2. When performing campaign performance analysis, consider metrics such as
   spend, impressions, clicks, CTR, CPC, conversions, conversion rate,
   and ROAS as appropriate.
3. Ground answers strictly in the provided data or tool results.
   Do not invent unavailable metrics.
4. If information required to answer the question is missing,
   clearly identify what information is needed.
5. Use available tools for data retrieval or calculations when appropriate.
"""


ads_agent = Agent(
    name="ads-data-analyst",

    description=(
        "Analyzes advertising datasets, campaign performance, and advertising metrics. "
        "Use for questions involving impressions, clicks, CTR, CPC, conversions, "
        "conversion rate, spend, ROAS, campaign comparison, and performance analysis."
    ),

    model=get_qwen_4b(),
    tools=[
        get_campaign_metrics,
    ],

    system_prompt=ADS_ANALYST_INSTRUCTIONS.strip(),
)

if __name__ == "__main__":
    result = ads_agent(
        "What are the performance metrics for campaign C003?"
    )

    print("\n===== TYPE =====")
    print(type(result))

    print("\n===== RESULT =====")
    print(result)

    print("\n===== ATTRIBUTES =====")
    print(dir(result))
    print("\n===== MESSAGE =====")

    print(result.message)
    print(type(result.message))

    print("\n===== STRUCTURED OUTPUT =====")
    print(result.structured_output)
    print(type(result.structured_output))