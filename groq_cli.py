import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt = " ".join(sys.argv[1:])

if not prompt:
    print("Usage: python groq_cli.py \"your prompt here\"")
    sys.exit(1)

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

print("\n--- Groq Response ---\n")
print(completion.choices[0].message.content)