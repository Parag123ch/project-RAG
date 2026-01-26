from langchain.tools import tool

@tool
def retrieve_documents(query, db):
    """Retreive relevant documents from the vector database based on the query."""
    try:
        relevant_docs = db.query(query_texts=[query], n_results=10)
        print(f"Number of documents retrieved: {len(relevant_docs)}")
        return "\n\n".join([doc.page_content for doc in relevant_docs])
    except Exception as e:
        print(f"Error retrieving documents: {e}")
        return None
    
retrieval_tool = retrieve_documents