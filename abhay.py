import os
from dotenv import load_dotenv

load_dotenv()
apikey1 = os.getenv("OPENAI_API_KEY", "")
