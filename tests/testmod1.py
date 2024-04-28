import requests

API_URL = "https://api-inference.huggingface.co/models/ac0hik/emotions_detection_french"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
print( query({
	"inputs": "Je n'aime pas ça.",
}))