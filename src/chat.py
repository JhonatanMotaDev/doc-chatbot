import os

from dotenv import load_dotenv
import google.generativeai as genai


def ask(context: str, question: str) -> str:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Variavel de ambiente GEMINI_API_KEY nao encontrada.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Responda com base apenas no contexto fornecido.\n\n"
        f"Contexto:\n{context}\n\n"
        f"Pergunta:\n{question}"
    )

    response = model.generate_content(prompt)
    return response.text or ""
