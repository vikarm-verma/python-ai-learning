import os
from pathlib import Path
from dotenv import load_dotenv


class GeminiConfig:

    def __init__(self):

        # Find the folder containing this file
        shared_folder = Path(__file__).resolve().parent

        # Find the .env file inside the shared folder
        env_file = shared_folder / ".env"

        # Load the shared .env file
        load_dotenv(env_file)

        # Read the Gemini API key
        self.api_key = os.getenv("GEMINI_API_KEY")

        # Raise an error if the key is missing
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY was not found.")
        else:
            print ("Key found")
# gcobject= GeminiConfig()