from langchain.chat_models import init_chat_model
from langgraph.graph import MessagesState

def generate_query_or_respond(MessageState, retrieval_tool):
    """Call the model to generate a response based on the message state by calling the retrieval tool or directly responding to the user."""
    try:
        response_model = init_chat_model("openai:o3-mini", temperature=0)
        response = (
            response_model.bind_tools([retrieval_tool]).invoke(input=MessageState['messages'])
        )
        print(f"Model response generated: {response}")
        return {"messages": response}
    except Exception as e:
        print(f"Error building context: {e}")
        return None
