import gradio as gr

from apps.gen_marketing.CONFIG import (
    campaign_options, 
    content_size, 
    business_size,
    industry,
)
from apps.gen_marketing.gen_marketing import (
    generate_headline,
    generate_main_content,
    generate_cta,
)
from apps.gen_marketing.utils import ( 
    update_content_log,
    filter_records,
    get_filtered_records,
)


def format_content_output(headline, description, cta):    
    return  f"""
    <h1>{headline}</h1>
    <p>{description}</p>
    <h2>{cta}</h2>
    """


def process_data(
    id_name,
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
    update_content_log(id_name, content_size, headline, description, cta)
    return format_content_output(headline, description, cta)


def main():
    interface = gr.Interface(
            fn=process_data,
            inputs=[
                gr.Textbox(label="ID / Name"),
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
            with gr.TabItem("Generating Content", id=0):
                with gr.Tabs():
                    interface.render()

            with gr.TabItem("Previous Content", id=1):
                id_name_filter_input = gr.Textbox(label="ID / Name")
                content_size_filter_input = gr.Textbox(label="Content Size")
                submit_btn = gr.Button("Submit")

                with gr.Column(visible=False) as output_col:
                    diagnosis_box = gr.Dataframe()

                def submit(id_filter, content_size_data):
                    filter_records(id_filter, content_size_data)
                    filtered_records = get_filtered_records()
                    return {
                        output_col: gr.Column(visible=True),
                        diagnosis_box: filtered_records,
                    }

                submit_btn.click(
                    submit,
                    [id_name_filter_input, content_size_filter_input],
                    [output_col, diagnosis_box],
                )

    app.launch(share=True)#, auth=("GENAIBCB", "GENAIBCBPWD"))
    
if __name__=="__main__":
    main()
    