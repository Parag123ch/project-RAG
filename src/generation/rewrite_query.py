from langchain.messages import HumanMessage
from langgraph.graph import MessagesState

from ..config.models import response_model

REWRITE_QUERY_PROMPT = (
    "Look at the input and try to reason about the underlying semantic intent / meaning.\n"
    "Here is the initial question:"
    "\n ------- \n"
    "{question}"
    "\n ------- \n"
    "Formulate an improved question:"
)

def rewrite_query(state: MessagesState):
    """Rewrite the original user query."""
    question = state["messages"][0].content
    try:
        prompt = REWRITE_QUERY_PROMPT.format(question=question)
        response = response_model.invoke({"role": "user", "content": prompt})
        print(f"Rewritten query generated: {response}")
        return {"messages": [HumanMessage(content=response.content)]}
    except Exception as e:
        print(f"Error rewriting query: {e}")
        return None