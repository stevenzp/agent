from llama_index.core import PromptTemplate

template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question: {query_str}\n"
)
qa_template = PromptTemplate(template)

# you can create text prompt (for completion API)
prompt = qa_template.format(context_str=..., query_str=...)

# or easily convert to message prompts (for chat API)
messages = qa_template.format_messages(context_str=..., query_str=...)

context = """Purpose: The primary role of this agent is to assist users by providing accurate information about the concepts in algorithmic game theory and deep learning"""