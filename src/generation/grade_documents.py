from pydantic import BaseModel, Field
from typing import Literal
from langchain.chat_models import init_chat_model

GRADE_PROMPT = (
    "You are a grader assessing relevance of a retrieved document to a user question. \n "
    "Here is the retrieved document: \n\n {context} \n\n"
    "Here is the user question: {question} \n"
    "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n"
    "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."
)

class GradeDocuments(BaseModel):
    """Grade retrieved documents for relevance to the user question."""
    score:str = Field(
        description="Relevance score: 'yes' if relevant, 'no' if not relevant"
    )

grader_model = init_chat_model("anthropic:claude-sonnet-4-5", temperature=0)

def grade_documents(MessageState) -> Literal["generate_answer", "rewrite_query"]:
    """Determine whether the retrieved documents are relevant to the question."""
    try:
        question = MessageState["messages"][0].content
        context = MessageState["messages"][-1].content
        prompt = GRADE_PROMPT.format(question=question, context=context)
        response = (
            grader_model.with_structured_output(GradeDocuments).invoke({"role": "user", "content": prompt})
        )
        score = response.score
        if score == "yes":
            return "generate_answer"
        else:
            return "rewrite_query"
    except Exception as e:
        print(f"Error grading documents: {e}")
        return "rewrite_query"

