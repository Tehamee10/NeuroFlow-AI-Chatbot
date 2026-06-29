from pinecone import Pinecone
from fastembed import TextEmbedding
from docx import Document
from dotenv import load_dotenv
import os
import uuid

# Load env
load_dotenv()

print("🚀 Starting Upload Script")

# Pinecone
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("servicebot")

# Lightweight embedding model
print("🧠 Loading embedding model...")
embedding_model = TextEmbedding()

# Read DOCX
print("📄 Reading document...")

doc = Document("NeuroFlow_Complete_Documentation.docx")

text = "\n".join([para.text for para in doc.paragraphs])

print("✅ Document loaded")
print("📚 Total characters:", len(text))

# Chunking
def split_text(text, chunk_size=500, overlap=100):
    chunks = []

    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks

chunks = split_text(text)

print(f"✂️ Total chunks: {len(chunks)}")

# Generate vectors
vectors = []

for i, chunk in enumerate(chunks):
    print(f"🧠 Embedding chunk {i+1}/{len(chunks)}")

    embedding = list(embedding_model.embed([chunk]))[0].tolist()

    vectors.append({
        "id": str(uuid.uuid4()),
        "values": embedding,
        "metadata": {
            "text": chunk,
            "chunk_number": i
        }
    })

# Upload
print("☁️ Uploading to Pinecone...")

batch_size = 50

for i in range(0, len(vectors), batch_size):
    batch = vectors[i:i + batch_size]

    index.upsert(vectors=batch)

    print(f"✅ Uploaded batch {i//batch_size + 1}")

print("🎉 Upload Complete!")
print(f"📦 Total vectors uploaded: {len(vectors)}")