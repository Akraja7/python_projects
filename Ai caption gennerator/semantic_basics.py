import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("messi.jpg")
print(output[0]["generated_text"])

