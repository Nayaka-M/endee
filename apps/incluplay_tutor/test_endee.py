from endee import Endee
import numpy as np

def get_vector(text):
    words = text.lower().split()
    vec = np.zeros(128)
    for w in words:
        vec[hash(w) % 128] += 1.0
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec.tolist()

def test_search():
    db = Endee("./endee_db")
    query = "what is photosynthesis"
    vec = get_vector(query)
    results = db.search(vec, top_k=3)
    print("Search results for:", query)
    for r in results:
        print("-", r)

if __name__ == "__main__":
    test_search()