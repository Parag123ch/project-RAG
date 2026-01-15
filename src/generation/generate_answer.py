from langgraph.graph import MessagesState

from ..config.models import answer_model

GENERATE_ANSWER_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. "
    "Use three sentences maximum and keep the answer concise.\n"
    "Question: {question} \n"
    "Context: {context}"
)

def generate_answer(state: MessagesState):
    """Generate a final answer based on the retrieved documents and the user question."""
    try:
        question = state["messages"][0].content
        context = state["messages"][-1].content
        prompt = GENERATE_ANSWER_PROMPT.format(question=question, context=context)
        response = answer_model.invoke({"role": "user", "content": prompt})
        print(f"Generated answer: {response}")
        return {"messages": [response]}
    except Exception as e:
        print(f"Error generating answer: {e}")
        return None