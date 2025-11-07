import os
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

generator = pipeline("text2text-generation", model="google/flan-t5-small")

llm = HuggingFacePipeline(pipeline=generator)

prompt = PromptTemplate.from_template(
    "You are a helpful and friendly AI assistant. Answer clearly.\nQuestion: {question}\nAnswer:"
)

chain = prompt | llm

while True:
    user_input = input("\nAsk me something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Bye Mehak! Have a great day")
        break
    response = chain.invoke({"question": user_input})
    print("Ans -> ", response)
