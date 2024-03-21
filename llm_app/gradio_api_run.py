import gradio as gr

from apps.gen_marketing.utils import remove_quote_marks
from apps.gen_marketing.CONFIG import llm_parameters
from GCP_CONFIG import GCP_llm

def gcp_llm_response(prompt):
    instances = [{"prompt": prompt}]
    response = GCP_llm.predict(instances=instances, parameters=llm_parameters).predictions[0]["content"]
    response = remove_quote_marks(response)
    return response


def main():
    api = gr.Interface(fn=gcp_llm_response, inputs="textbox", outputs="textbox")
    api.launch(share=True, auth=("GENAIBCB", "GENAIBCBPWD"))
    
if __name__=="__main__":
    main()
    