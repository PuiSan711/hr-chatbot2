from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import os

app = FastAPI()

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "sk-..."  # Replace with your actual OpenAI API key

# Load and embed documents from the ./docs directory
loader = DirectoryLoader("./docs", glob="**/*.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

embedding = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embedding)

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=db.as_retriever(),
    return_source_documents=True
)

class QueryRequest(BaseModel):
    question: str
    language: str = "en"

@app.post("/chat")
def chat(query: QueryRequest):
    user_question = query.question
    answer = qa_chain.run(user_question)
    return {"answer": answer}
