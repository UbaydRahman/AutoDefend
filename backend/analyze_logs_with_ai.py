import boto3
import json
import os
from config import AWS_REGION, BEDROCK_MODEL_ID
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client('bedrock-runtime', region_name=AWS_REGION)

def call_claude(log):
    prompt = f"""
    Analyze the following security log and respond in JSON.

    Log:
    {json.dumps(log)}

    Return a JSON object with:
    - action: "Block", "Monitor", or "Ignore"
    - severity: "High", "Medium", or "Low"
    - reason: A short one-line reason
    - recommended_prevention: Advice to help prevent this type of attack in the future
    """

    body = {
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens": 500,
        "temperature": 0.2,
        "top_k": 250,
        "top_p": 1.0,
        "stop_sequences": ["\n\nHuman:"]
    }

    response = bedrock.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read().decode())
    return json.loads(result['completion'])

def analyze_logs():
    with open("../logs/fake_logs.json") as f:
        logs = json.load(f)

    results = []
    for log in logs[:10]:  # Start with 10 for test purposes
        print(f"Analyzing log ID: {log['id']}")
        ai_response = call_claude(log)
        log['ai_decision'] = ai_response
        results.append(log)

    with open("../reports/ai_decisions.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Analysis complete. Saved to ai_decisions.json")

if __name__ == "__main__":
    analyze_logs()
