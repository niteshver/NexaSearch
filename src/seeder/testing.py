import rank_bm25
from rank_bm25 import BM25Okapi

documents = [
    "Python is a programming language",
    "Teri programming python",
    "Language python programming"
]

split_data = [doc.lower().split() for doc in documents]

bm25 = BM25Okapi(split_data)

query = "wht is python?"

tokenzine_query = query.lower().split()
scpre = bm25.get_scores(tokenzine_query)

print(scpre)

best_doc = documents[scpre.argmax()]
print(best_doc)
