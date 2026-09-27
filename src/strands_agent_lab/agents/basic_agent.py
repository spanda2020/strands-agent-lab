from strands import Agent

from strands_agent_lab.models.local_models import get_qwen_4b


BASIC_AGENT_INSTRUCTIONS = """
You are a helpful general-purpose AI assistant.

Answer general knowledge and everyday questions clearly and concisely.
"""


basic_agent = Agent(
    name="basic-agent",

    description=(
        "Handles general knowledge and everyday questions that do not "
        "require a specialized domain agent."
    ),

    model=get_qwen_4b(),

    system_prompt=BASIC_AGENT_INSTRUCTIONS.strip(),
)


if __name__ == "__main__":
    response = basic_agent(
        "What is the capital of Japan?"
    )

    print(response)