from strands import Agent

from strands_agent_lab.agents.basic_agent import basic_agent
from strands_agent_lab.agents.ads_agent import ads_agent
from strands_agent_lab.models.local_models import get_qwen_4b


ORCHESTRATOR_INSTRUCTIONS = """
You are an orchestrator responsible for routing user requests
to the appropriate specialist agent.

Delegate advertising-related questions to the ads data analyst.

Delegate general questions to the basic agent.

Do not perform specialist work yourself when an appropriate
agent is available.
"""


orchestrator = Agent(
    name="orchestrator",

    description=(
        "Routes user requests to the appropriate specialist agent."
    ),

    model=get_qwen_4b(),

    system_prompt=ORCHESTRATOR_INSTRUCTIONS.strip(),

    tools=[
        basic_agent.as_tool(),
        ads_agent.as_tool(),
    ],
)


if __name__ == "__main__":
    question = input("Ask me something: ")

    result = orchestrator(question)

    print("\nResponse:")
    print(result)

    print("\n===== METRICS / TRACE =====")
    print(result.metrics.get_summary())