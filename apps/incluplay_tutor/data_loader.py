from endee import Endee
import numpy as np

def get_vector(text: str):
    words = text.lower().split()
    vec = np.zeros(128)
    for w in words:
        vec[hash(w) % 128] += 1.0
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec.tolist()

NCERT_CHUNKS = [
    {"id": "sci_1", "text": "Photosynthesis uses sunlight water and CO2 to make food in plants.", "subject": "Science"},
    {"id": "sci_2", "text": "Mitochondria is the powerhouse of the cell producing ATP energy.", "subject": "Science"},
    {"id": "math_1", "text": "Pythagorean theorem a squared plus b squared equals c squared.", "subject": "Mathematics"},
    {"id": "tamil_1", "text": "Thirukkural by Thiruvalluvar has 1330 kurals in three sections.", "subject": "Tamil"},
    {"id": "evs_1", "text": "Deforestation causes biodiversity loss and climate change.", "subject": "EVS"},
]

def load_data():
    db = Endee("./endee_db")
    for chunk in NCERT_CHUNKS:
        vec = get_vector(chunk["text"])
        db.add(id=chunk["id"], vector=vec, metadata=chunk)
    print("Loaded", len(NCERT_CHUNKS), "chunks into Endee!")

if __name__ == "__main__":
    load_data()