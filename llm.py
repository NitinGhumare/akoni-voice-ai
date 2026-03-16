from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("prompts/system_prompt.txt", encoding="utf-8") as f:
    system_prompt = f.read()


def stream_response(messages, model_name):

    stream = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.3,
        stream=True
    )

    for chunk in stream:

        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content