import gradio as gr

def greet(name):
    return "Hello " + name + "!"



def main():
    print("Hello from ai-drafting-assistant!")
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()


if __name__ == "__main__":
    main()
