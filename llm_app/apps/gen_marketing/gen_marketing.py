from ctransformers import AutoModelForCausalLM

from apps.gen_marketing.CONFIG import (
    content_size,
    llm_parameters,
    LOCAL_MODEL,
    LOCAL_MODEL_PATH,
    LOCAL_MODEL_TYPE,
)

if LOCAL_MODEL:
    llm = AutoModelForCausalLM.from_pretrained(
        LOCAL_MODEL_PATH,
        model_type=LOCAL_MODEL_TYPE,
    )
    prompt_prefix = ""
else:
    from GCP_CONFIG import GCP_llm
    llm = GCP_llm
    prompt_prefix = (
        "You work for a bank creating marketing content. "
        "The tone of voice must be quietly confident, expert "
        "and empathetic. "
    )
    

def generate_llm_response(prompt):
    if LOCAL_MODEL:
        response = llm(prompt)
    else:
        instances = [{"prompt": prompt}]
        response = llm.predict(instances=instances, parameters=llm_parameters).predictions[0]["content"]
    response = remove_quote_marks(response)
    return response


def remove_quote_marks(string):
    while string[0] in ["\'", '\"', " ", r"\\"]:
        string = string[1:]
    while string[-1] in ["\'", '\"', " ", r"\\"]:
        string = string[:-1]
    return string


def create_marketing_content(
        product,
        material_size,
        business_size,
        industry,
        aim,
):
    """
    Given input about how you want the commercial marketing 
    material to look, this function returns the text 
    for some marketing
    """
    headline = generate_headline(
        product,
        business_size,
        industry,
        aim,
    )
    description = generate_main_content(
        headline, 
        product,
        material_size,
        business_size,
        industry,
        aim,
    )
    cta = generate_cta(description)

    return {
        "headline": headline,
        "description": description,
        "cta": cta,
    }


def generate_headline(
        product,
        business_size,
        industry,
        aim,
):
    if aim != "":
        aim = f"Aim: '{aim}', "
    else:
        aim=""

    headline_prompt = prompt_prefix + (
        "You work for a bank creating marketing content. Using the following features to guide you, "
        "create a headline between 2 and 7 words for the business banking ad. "
        f"Product: '{product}', "
        f"{aim}"
        f"Busines size: '{business_size}', "
        f"Industry: '{industry}'. "
        "The business banking ad headline is:"
    )
    return generate_llm_response(headline_prompt)
    

def generate_main_content(
        headline,
        product,
        material_size,
        business_size,
        industry,
        aim,
):
    main_content_prompt = prompt_prefix + (
        "You work for a bank creating marketing content. Using the following features to guide you, "
        "create the main content for the business banking ad"
        f"campaign {material_size}. "
        f"Headline: '{headline}', "
        f"Product: '{product}', "
        f"{aim}"
        f"Busines size: '{business_size}', "
        f"Industry: '{industry}'. "
        f"The ad campaign main content {material_size} is:"
    )
    return generate_llm_response(main_content_prompt)


def generate_cta(main_content):
    cta_prompt = (
        "You work for a bank creating marketing content. Using the following ad content, "
        "create a call to action between 1 and 5 words." 
        f"CONTENT: {main_content}"
        "CALL TO ACTION:"
    )
    return generate_llm_response(cta_prompt)


def change_llm_output(component, component_name, change):
    change_output_prompt = prompt_prefix + (
        f"Edit this {component_name} of an ad campaign to "
        f"{change}. The {component_name} is: '{component}'. The change "
        f"of '{change}' is:"
    )
    return generate_llm_response(change_output_prompt)
