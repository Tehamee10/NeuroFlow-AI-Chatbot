from pinecone import Pinecone
from fastembed import TextEmbedding
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

print("🤖 NeuroFlow Chatbot Started")

# Pinecone setup
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("servicebot")

# Embedding model
embedding_model = TextEmbedding()

while True:
    query = input("\n🧑 You: ")

    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    print("🧠 Searching...")

    # Generate embedding
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
        print("🤖 No answer found.")
        continue

    best_match = matches[0]

    answer = best_match["metadata"]["text"]

    print("\n🤖 Bot Answer:\n")
    print(answer)