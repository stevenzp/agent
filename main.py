from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from note_engine import note_engine
from prompts import context
from pdf import pdf_query_engine

load_dotenv()

tools=[
    note_engine,
    QueryEngineTool(
        query_engine=pdf_query_engine,
        metadata=ToolMetadata(
            name="background_information",
            description="this gives detailed information about recent advancements in algorithmic game theory"
        ),
    )
]
llm = OpenAI(model = "gpt-4o")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)


while(prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)


