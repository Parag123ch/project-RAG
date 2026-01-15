from langchain.chat_models import init_chat_model

grader_model = init_chat_model("anthropic:claude-sonnet-4-5", temperature=0)
response_model = init_chat_model("openai:o3-mini", temperature=0)