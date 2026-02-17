import os
from groq import Groq
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_agent(message, history):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Zoupie's Groq AI assistant."},
            *history,
            {"role": "user", "content": message}
        ]
    )
    reply = completion.choices[0].message.content
    return reply

with gr.Blocks(theme=gr.themes.Monochrome(), title="zoupies_groq_ai") as app:
    gr.Markdown("# zoupies_groq_ai")
    gr.Markdown("A clean GPT-style interface for your Groq AI agent")

    chatbot = gr.Chatbot(height=500)
    msg = gr.Textbox(
        placeholder="Type your message and press Enter...",
        show_label=False
    )

    msg.submit(chat_with_agent, [msg, chatbot], chatbot)
    msg.submit(lambda: "", None, msg)  # clear input after send

app.launch(server_name="0.0.0.0", server_port=7860)
