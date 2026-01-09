from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunker(docs):
    docs_list = [item for sublist in docs for item in sublist]
    try:
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            "gpt2",
            chunk_size=1000,
            chunk_overlap=200
        )
        doc_splits = text_splitter.split_documents(docs_list)
        print(f"Number of chunks created: {len(doc_splits)}")
        return doc_splits
    except Exception as e:
        print(f"Error during chunking: {e}")
        return None

