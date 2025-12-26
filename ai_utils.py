import os
from openai import OpenAI

def summarize_text(text):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "AI summary unavailable."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that summarizes notes into clear, concise bullet points. "
                    "Always return 3–5 bullet points using hyphens (-). No paragraphs."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        max_tokens=180,
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
