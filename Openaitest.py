import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", "")

response = openai.Completion.create(
 model="text-davinci-003",
 prompt="Write an email to my boss for resignation?",
 temperature=0.7,
 max_tokens=256,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0
)

print(response)