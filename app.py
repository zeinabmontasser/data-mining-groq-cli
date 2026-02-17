import os
from groq import Groq
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_agent(prompt):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

app = gr.Interface(
    fn=chat_with_agent,
    inputs=gr.Textbox(lines=4, placeholder="Type your prompt here..."),
    outputs="text",
    title="Groq AI Agent",
    description="Your CLI agent, now with a web interface"
)
app = gr.Blocks(theme=gr.themes.Monochrome())


app.launch(server_name="0.0.0.0", server_port=7860, root_path="/zoupies_groq_ai")

