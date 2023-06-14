from transformers import pipeline
import gradio as gr

<<<<<<< HEAD
# I add a comt
# Initialize the summarization model
model = pipeline("summarization")

=======

model = pipeline(
    "summarization",
)
>>>>>>> refs/remotes/origin/main

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


# create an interface for the model
with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()
