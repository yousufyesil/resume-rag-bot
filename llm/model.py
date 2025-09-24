
from ollama import ChatResponse, chat

from llm.query import ask_vdb

# 1) Nutzerfrage definieren (eine Quelle für Retrieval und Prompt)
user_query = input("Ask me something: ")

# 2) Retrieval: Passagen aus der vDB holen
context_passages = ask_vdb(query=user_query, debug=False)  # gibt list[str] zurück

# 3) Minimalen Prompt bauen: Kontext + Frage
prompt = "Kontext:\n"
if context_passages:
    prompt += "\n\n".join(context_passages)
else:
    prompt += "(Keine passenden Passagen gefunden.)"
prompt += f"\n\nFrage:\n{user_query}\n"

# 4) LLM mit dem Prompt aufrufen
response_stream: ChatResponse = chat(
    model="mistral:7b",
    messages=[
        {
            "role": "system",
            "content": """Du bist die virtuelle Kopie mit dem Namen "Yousuf". """
                       "Deine Aufgabe ist es höfliche und profesionell Fragen zu deiner Person zu beantworten."
                        "Anfragen können möglicherweise von Recruiter kommen. Versuch daher subtil eindruck zu erreichen und hebe kompetenzen hervor"
                       "Wenn keine Information vorhanden ist, sag das klar. "
                       
                       "Antworten bitte kurz und auf Deutsch."

        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    stream=True

)

for chunk in response_stream:
    # jedes "chunk" ist ein Stück vom Modell
    print(chunk['message']['content'], end="", flush=True)

def ask(model :str, prompt :str) -> str:

    SYSTEM_PROMPT : str = \
    """
    Du bist die virtuelle Kopie mit dem Namen "Yousuf".
    Deine Aufgabe ist es höfliche und professionell Fragen zu deiner Person zu beantworten.
    Anfragen können möglicherweise von Recruiter kommen. Versuch daher subtil Eindruck zu erreichen und hebe kompetenzen hervor.
    Wenn keine Information vorhanden ist, sag das klar.
    Antworten bitte kurz aber mit relevanten Details und auf Deutsch.
    """
    #TODO Chat in Funktion kapseln
    return ""