from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class ClassifierAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def classify(self, email_text):
        prompt = f"""
You are an AI assistant trained to classify customer emails.

Return JSON with:
- category: ["ORDER", "CANCEL", "SHIPPING", "INVOICE", "COMPLAINT", "GENERAL"]
- intent: like "track_order", "cancel_order", etc.

Email:
\"\"\"{email_text}\"\"\"
"""
        result = self.llm.invoke(prompt)
        try:
            return eval(result.content.strip())
        except Exception as e:
            print("Classification failed:", e)
            return {"category": "GENERAL", "intent": "unknown"}
