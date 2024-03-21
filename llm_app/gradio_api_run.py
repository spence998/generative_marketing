import gradio as gr

from apps.gen_marketing.gen_marketing import generate_llm_response


def main():
    api = gr.Interface(fn=generate_llm_response, inputs="textbox", outputs="textbox")
    api.launch(share=True, auth=("GENAIBCB", "GENAIBCBPWD"))
    
if __name__=="__main__":
    main()
    