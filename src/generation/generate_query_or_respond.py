from langgraph.graph import MessagesState

from ..config.models import response_model

def generate_query_or_respond(state: MessagesState, retrieval_tool):
    """Call the model to generate a response based on the message state by calling the retrieval tool or directly responding to the user."""
    try:
        response = (
            response_model.bind_tools([retrieval_tool]).invoke(input=state['messages'])
        )
        print(f"Model response generated: {response}")
        return {"messages": response}
    except Exception as e:
        print(f"Error building context: {e}")
        return None