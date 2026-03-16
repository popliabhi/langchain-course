from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def main():
    print("Hello from langchain-course!")
    #print(os.environ.get("OPENAI_API_KEY"))
    information = input("Enter details to get summary: ")
    #print(f"You entered: {information}")

    summary = """You are a helpful assistant that can answer questions about the following information: {information}. 
    I want summarize text in bullent points"""
    
    prompt = ChatPromptTemplate.from_template(summary)
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    chain = prompt | model
    response = chain.invoke({"information": information})
    
    print(response.content)


if __name__ == "__main__":
    main()
