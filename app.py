from transformers import pipeline
import gradio as gr

#add cmt
model = pipeline(
    "summarization",
)

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# create an interface for the model
with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()
