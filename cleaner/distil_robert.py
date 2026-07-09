import json
from sentence_transformers import SentenceTransformer

# 1. Load the model
model = SentenceTransformer("sentence-transformers/all-distilroberta-v1")

web_pages = [
    "Crawl4AI is an asynchronous web scraping engine built for AI extraction.",
    "xxHash is a non-cryptographic hash function working at RAM speed limits.",
]

# 2. Generate vectors
embeddings = model.encode(web_pages, show_progress_bar=True)

print(f"Generated {len(embeddings)} vectors.")
print(f"Vector structure dimension: {embeddings[0].shape}")

# 3. Check if embeddings were successfully created and contain data
if embeddings is not None and len(embeddings) > 0:
    # NumPy arrays must be converted to Python lists to be JSON serializable
    embeddings_as_list = embeddings.tolist()

    with open("trns.json", "w", encoding="utf-8") as file:
        json.dump(embeddings_as_list, file, indent=4)
    print("Teri maa ka bosda")
else:
    raise ValueError("Gand mra")
