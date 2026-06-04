import requests

url = "http://localhost:11434/api/generate"
prompt = input("Enter your question: ")

payload = {
    "model": "qwen3:4b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)
print("\nModel Response:\n", response.json()["response"])