from fastapi import FastAPI
from pydantic import BaseModel
from pinecone import Pinecone
from fastembed import TextEmbedding
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import os

# Load environment variables
load_dotenv()

# FastAPI app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pinecone setup
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("servicebot")

# Gemini setup
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Embedding model
embedding_model = TextEmbedding()

# Request model
class QueryRequest(BaseModel):
    query: str

# Home route
@app.get("/")
def home():
    return {
        "message": "NeuroFlow Chatbot API Running"
    }

# Chat route
@app.post("/chat")
def chat(request: QueryRequest):

    try:

        query = request.query

        # Create embedding
        query_embedding = list(
            embedding_model.embed([query])
        )[0].tolist()

        # Search Pinecone
        results = index.query(
            vector=query_embedding,
            top_k=3,
            include_metadata=True
        )

        matches = results.get("matches", [])

        if not matches:
            return {
                "answer": "No relevant information found."
            }

        # Get context
        context = "\n".join(
            [
                match["metadata"]["text"]
                for match in matches
            ]
        )

        # Prompt
        prompt = f"""
        You are a professional AI assistant.

        ONLY answer from the provided context.

        If the answer is not in the context,
        say:
        'This question is not related to the uploaded document.'

        Context:
        {context}

        Question:
        {query}
        """

        # Gemini response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "answer": response.text
        }

    except Exception as e:

        return {
            "answer": str(e)
        }