from google.cloud import aiplatform
import vertexai
from vertexai import preview
from vertexai.preview.language_models import TextGenerationModel

import os

import gradio as gr

from apps.gen_marketing.CONFIG import campaign_options, content_size, business_size, industry
from apps.gen_marketing.gen_marketing import (
    generate_headline,
    generate_main_content,
    generate_cta,
    remove_quote_marks,
)

def generate_llm_response(prompt):
    instances = [
        {"prompt": prompt},    
    ]
    parameters = {
        "temperature":0.8,
        "topK": 40,
    }
    return endpoint.predict(
        instances=instances,
        parameters=parameters,
    ).predictions[0]["content"]


def format_content_output(headline, description, cta):
    headline = remove_quote_marks(headline)
    description = remove_quote_marks(description)
    cta = remove_quote_marks(cta)
    
    return  f"""
    <h1>{headline}</h1>
    <p>{description}</p>
    <h2>{cta}</h2>
    """


def process_data(
    campaign_options,
    content_size,
    business_size,
    industry,
    aim,
):
    headline = generate_headline(
        campaign_options,
        business_size,
        industry,
        aim,
    )
    description = generate_main_content(
        headline, 
        campaign_options,
        content_size,
        business_size,
        industry,
        aim,
    )
    cta = generate_cta(description)
    return format_content_output(headline, description, cta)


def main():

    # For if you are running in a notebook
    # if not os.getenv("IS_TESTING"):
        # shell_output=!gcloud config list --format 'value(core.project)' 2>/dev/null
        # PROJECT_ID = shell_output[0]
        # print("Project ID: ", PROJECT_ID)
    # else:
    # For if you are running as a script
    PROJECT_ID = "playpen-fa38ad"

    BUCKET_NAME="playpen-basic-gcp_dv_npd-" + PROJECT_ID + "-bucket"
    BUCKET_URL="gs://" + BUCKET_NAME
    print("Bucket NAME: ", BUCKET_NAME)
    print("Bucket URL: ", BUCKET_URL)

    REGION = 'europe-west2'  # London

    SERVICE_ACCOUNT = "playpen-fa38ad-consumer-sa@playpen-fa38ad.iam.gserviceaccount.com" 

    aiplatform.init(project=PROJECT_ID, location=REGION)

    endpoint_name = "projects/689526501683/locations/europe-west2/endpoints/2361214414788493312" 
    aip_endpoint_name = endpoint_name
    endpoint = aiplatform.Endpoint(aip_endpoint_name)
    
    interface = gr.Interface(
        fn=process_data,
        inputs=[
            gr.Dropdown(choices=campaign_options, value="Fraud", label="Product"),
            gr.Dropdown(choices=content_size.keys(), value="Medium", label="Content size"),
            gr.Dropdown(choices=business_size, value="Any", label="Business size for content"),
            gr.Dropdown(choices=industry, value="Any", label="Industry"),
            gr.Textbox(label="Aim for content:"),
        ],
        outputs="html",
    )

    with gr.Blocks(
        theme=gr.themes.Default(
            primary_hue=gr.themes.colors.emerald,
        )
    ) as app:
        with gr.Tabs():
                gr.HTML(
                    value="""
                    <div style='text-align:center;'>
                        <h1>Generative Commercial Marketing</h1>
                    <div>
                    """,
                    label=" ",
                )
        with gr.Tabs():
            interface.render()

    app.launch(share=True)
    
    
if __name__=="__main__":
    main()
    