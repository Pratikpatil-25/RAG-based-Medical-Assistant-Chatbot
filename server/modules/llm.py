from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def get_llm_chain(retriever):

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system", """
                                You are MediBot, an AI-powered assistant trained to help users understand
                                medical documents and answer health-related questions.

                                Answer ONLY using the provided context.

                                Rules:
                                - Be clear, factual, and respectful.
                                - Use simple language whenever possible.
                                - If the answer is not present in the context, say:
                                "I'm sorry, but I couldn't find relevant information in the provided documents."
                                - Never make up facts.
                                - Never provide diagnoses or medical advice.

                                Context:
                                {context}
                            """
            ),
            (
                "human", "{input}"
            )
        ]
    )

    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain