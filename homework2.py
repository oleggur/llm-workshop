from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

prompt = "What's the formula for energy?"

def llm(prompt):
    response = client.chat.completions.create(
        model="gemma:2b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content

print(llm(prompt))