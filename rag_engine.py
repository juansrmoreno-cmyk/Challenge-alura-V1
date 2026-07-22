import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

VECTOR_DB_PATH = "./vector_db"
PDF_PATH = "documento_empresa.pdf"


def update_vector_db():
    """Lee el PDF y crea la base vectorial."""

    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"No existe {PDF_PATH}")

    print("Cargando PDF...")

    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    splits = text_splitter.split_documents(docs)

    print("Modelo de embedding: models/gemini-embedding-001")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    print("Creando índice FAISS...")

    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )

    vectorstore.save_local(VECTOR_DB_PATH)

    print("✅ Base vectorial creada correctamente.")


def get_answer(question: str):

    if not os.path.exists(VECTOR_DB_PATH):
        return "⚠️ La base de conocimiento está vacía."

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-3.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
         convert_system_message_to_human=True
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Responde únicamente usando el contexto proporcionado. "
            "Si la respuesta no está en el documento, responde que no existe información disponible.\n\n{context}"
        ),
        (
            "human",
            "{input}"
        )
    ])

    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    response = rag_chain.invoke(
        {
            "input": question
        }
    )

    return response["answer"]