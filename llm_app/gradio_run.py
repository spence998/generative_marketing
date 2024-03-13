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


def format_content_output(headline, description, cta):    
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
    