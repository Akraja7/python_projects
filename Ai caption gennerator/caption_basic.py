import requests

API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Question: Which is the largest city in the world? Answer:",
})

print(output[0]['generated_text'])