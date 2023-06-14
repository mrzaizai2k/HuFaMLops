from transformers import pipeline
import gradio as gr
# I add cmt

# Initialize the summarization model
model = pipeline("summarization")


def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


# Create a Gradio interface
interface = gr.Interface(fn=predict, inputs=gr.Textbox(placeholder="Enter text to summarize", lines=4), outputs="text")


# Launch the interface
interface.launch()

