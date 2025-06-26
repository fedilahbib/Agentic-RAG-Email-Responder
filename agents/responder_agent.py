from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class ResponderAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_response(self, email_text, context):
        prompt = f"""
You are an AI email assistant.

Email: "{email_text}"
Relevant info: "{context}"

Reply in a helpful, professional tone.
"""
        result = self.llm.invoke(prompt)
        return result.content
