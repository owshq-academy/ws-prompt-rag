from dotenv import load_dotenv
from langchain_openai import OpenAI
from src.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence

def main():
    # Load .env with your OPENAI_API_KEY
    load_dotenv()

    # Instantiate the LLM
    llm = OpenAI(temperature=0.7)

    # Define your prompt template
    prompt = PromptTemplate(
        input_variables=["question"],
        template="You are a helpful assistant. Q: {question}\nA:",
    )

    # Compose prompt + llm as a single runnable pipeline
    pipeline = RunnableSequence(prompt, llm)

    # Invoke it
    question = "What's 2+2, and why is it that number?"
    result = pipeline.invoke({"question": question})

    print(f">>> Q: {question}\n>>> A: {result}")

if __name__ == "__main__":
    main()