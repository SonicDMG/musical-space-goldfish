# api.py

import requests

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "37fb0878-2f37-4245-b1c9-bfb7b47b5036"
FLOW_ID = "ab55e139-5cad-478f-befb-6be389913c33"
APPLICATION_TOKEN = "AstraCS:JGaBXYMssWLegziRaqOtZNmJ:bf10a66f98b89be83c2a4c442c73f59458104b60bd0f8b7e4391c5ae82061a66"
ENDPOINT = "" # You can set a specific endpoint name in the flow settings

def run_flow(message: str, endpoint: str, application_token: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def get_bot_response(user_input):
    response = run_flow(user_input, ENDPOINT or FLOW_ID, APPLICATION_TOKEN)
    try:
        message = response['outputs'][0]['outputs'][0]['results']['message']['text']
    except (KeyError, IndexError):
        message = "No response from the API."
    return message
