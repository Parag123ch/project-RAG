from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

from ..generation.generate_query_or_respond import generate_query_or_respond
from ..rag.retriever import retrieval_tool
from ..generation.grade_documents import grade_documents
from ..generation.rewrite_query import rewrite_query
from ..generation.generate_answer import generate_answer

workflow = StateGraph(MessagesState)

workflow.add_node(generate_query_or_respond)
workflow.add_node("retrieve", ToolNode[retrieval_tool])
workflow.add_node(rewrite_query)
workflow.add_node(generate_answer)

workflow.add_edge(START, "generate_query_or_respond")

workflow.add_conditional_edges(
    "generate_query_or_respond",
    tools_condition,
    {
        "tools": "retrieve",
        END: END,
    },
)

workflow.add_conditional_edges(
    "retrieve",
    grade_documents,
)

workflow.add_edge("generate_answer", END)
workflow.add_edge("rewrite_query", "generate_query_or_respond")

graph = workflow.compile()