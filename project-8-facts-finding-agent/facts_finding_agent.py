from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from langchain_core.rate_limiters import InMemoryRateLimiter

FACTS = {
    "capital of france": "Paris",
    "largest ocean": "Pacific Ocean",
    "inventor of telephone": "Alexander Graham Bell",
    "population of india": "1.45 billion"
}

@tool
def get_fact(query: str) -> str:
    """
    Retrieves a fact from a predefined list. The query must be a match to one of the available facts.
    Available facts are:
    - "capital of france"
    - "largest ocean"
    - "inventor of telephone"
    - "population of india"
    """
    return FACTS.get(query.lower(), "Fact not found")

def run_data_retrieval_agent():
    """
    Creates an agent that can use the get_fact tool.
    """
    llm = ChatOllama(model="gemma3:4b").with_retry()
    tools = [get_fact]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    responses = []
    print("\n---Query 1: Capital of France ---")
    responses.append(agent_executor.invoke({"input": "What is the capital of France?"}))

    print("\n---Query 2: Inventor of telephone ---")
    responses.append(agent_executor.invoke({"input": "Who invented the telephone?"}))

    print("\n\n--- Final Agent Answers ---")
    for i, response in enumerate(responses, 1):
        print(f"Response {i}: {response['output']}")

if __name__ == "__main__":
    run_data_retrieval_agent()