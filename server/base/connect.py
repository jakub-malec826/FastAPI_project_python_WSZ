import certifi
from motor import motor_asyncio as motor
import os
from dotenv import load_dotenv

load_dotenv()

uri = f"mongodb+srv://admin:{os.getenv('MONGO_PASS')}@instructors.yfw6pdw.mongodb.net/?retryWrites=true&w=majority"

client = motor.AsyncIOMotorClient(uri, tlsCAFile=certifi.where())

db = client["INSTRUCTORS"]

print("Connected to Mongo")
