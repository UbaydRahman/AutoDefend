from config import AWS_REGION, BEDROCK_MODEL_ID

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "AutoDefend backend is alive and ready."
    }

if __name__ == "__main__":
    print("Running locally — Claude model:", BEDROCK_MODEL_ID)