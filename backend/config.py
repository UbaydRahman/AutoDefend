import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID")
BEDROCK_API_ROLE_ARN = os.getenv("BEDROCK_API_ROLE_ARN")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")
