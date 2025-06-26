from agents.email_sender_agent import EmailSenderAgent
from agents.loader_agent import LoaderAgent
from agents.indexer_agent import IndexerAgent
from agents.classifier_agent import ClassifierAgent
from agents.retriever_agent import RetrieverAgent
from agents.responder_agent import ResponderAgent
from dotenv import load_dotenv
import os

load_dotenv()

def agentic_rag_pipeline_with_email(email_text, recipient_email):
    # Agents
    loader = LoaderAgent()
    indexer = IndexerAgent()
    classifier = ClassifierAgent()
    responder = ResponderAgent()

    # Load and index KB
    kb = loader.load_knowledge_base("kb.csv")
    collection, embedder = indexer.index_documents(kb)
    retriever = RetrieverAgent(embedder)

    # Classify email
    classification = classifier.classify(email_text)
    print("Classification:", classification)

    # Retrieve relevant answer
    context = retriever.retrieve_answer(collection, query=classification['intent'])
    print("Retrieved Context:", context)

    # Generate reply
    reply = responder.generate_response(email_text, context)
    print("Reply:", reply)

    # Email sending config
    smtp_config = {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "smtp_user": os.getenv("EMAIL_ADDRESS"),
        "smtp_password": os.getenv("EMAIL_PASSWORD") 
    }

    email_agent = EmailSenderAgent(**smtp_config)
    email_agent.send_email(
        to_email=recipient_email,
        subject=f"Response regarding your {classification['category'].lower()} request",
        body=reply
    )

    return reply

recipient="exeample@exeample.com"
email_text = "Hi, I want to track my order placed last week. Can you help me?"
agentic_rag_pipeline_with_email(email_text, recipient)
