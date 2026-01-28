import gradio as gr

def greet(name):
    return f"Hello, {name}! Hope Gradio is Working Fine!!!"

demo = gr.Interface(
    fn = greet,
    inputs = gr.Textbox(label="Your Name"),
    outputs = gr.Textbox(label="Output"),
    title = "Week 8 - DAY 1: HeadStart with Gradio",
)

if __name__ == "__main__":
    demo.launch()