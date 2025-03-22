from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_sentence():
    response = client.get("/api/sentence")
    assert response.status_code == 200
    assert "sentence" in response.json()
    sentence = response.json()["sentence"]
    # Check if sentence ends with a period
    assert sentence.endswith(".")
    # Check if sentence starts with a capital letter
    assert sentence[0].isupper()
    # Count words (split by space and remove period)
    words = sentence[:-1].split()
    assert len(words) == 20 