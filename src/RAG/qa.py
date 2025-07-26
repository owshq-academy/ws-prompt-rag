from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from .retriever import build_retriever

def run_qa(query: str, use_pinecone: bool = True) -> str:
    retriever = build_retriever(use_pinecone=use_pinecone)
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa.run(query)