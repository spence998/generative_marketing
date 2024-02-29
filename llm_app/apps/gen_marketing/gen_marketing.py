from apps.gen_marketing.CONFIG import content_size


def generate_llm_response(prompt):
    return prompt


def create_marketing_content(
        topic,
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
        topic,
        business_size,
        industry,
        aim,
    )
    description = generate_main_content(
        headline, 
        topic,
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
        topic,
        business_size,
        industry,
        aim,
):
    if aim == "":
        aim = f"Aim: '{aim}', "
    else:
        aim=""

    headline_prompt = (
        "You work for a bank creating marketing content. "
        "The tone of voice must be quietly confident, expert "
        "and empathetic. Using the following features to guide you, "
        "create a headline for the business banking ad campaign. "
        f"Topic: '{topic}', "
        f"'{aim}'"
        f"Busines size: '{business_size}', "
        f"Industry: '{industry}'. "
        "The ad campaign headline is:"
    )

    return generate_llm_response(headline_prompt)
    

def generate_main_content(
        headline,
        topic,
        material_size,
        business_size,
        industry,
        aim,
):
    main_content_prompt = (
        "You work for a bank creating marketing content. "
        "The tone of voice must be quietly confident, expert "
        "and empathetic. Using the following features to guide you, "
        "create the main content for the business banking ad "
        f"campaign {content_size[material_size]}. "
        f"Headline: '{headline}', "
        f"Topic: '{topic}', "
        f"'{aim}'"
        f"Busines size: '{business_size}', "
        f"Industry: '{industry}'. "
        f"The ad campaign main content {content_size[material_size]} is:"
    )
    return generate_llm_response(main_content_prompt)


def generate_cta(main_content):
    cta_prompt = (
        "You work for a bank creating marketing content. "
        "The tone of voice must be quietly confident, expert "
        "and empathetic. Using the following ad content, "
        "create a call to action. E.g. "
        "<CONTENT>: 'You can make a payment to an existing payee in our app'"
        "<CALL TO ACTION>: 'Download the app'"
        f"<CONTENT>: {main_content}"
        "<CALL TO ACTION>:"
    )
    return generate_llm_response(cta_prompt)


def change_llm_output(component, component_name, change):
    change_output_prompt = (
        "You work for a bank creating marketing content. "
        "The tone of voice must be quietly confident, expert "
        f"and empathetic. Edit this {component_name} of an ad campaign to "
        f"{change}. The {component_name} is: '{component}'. The change "
        f"of '{change}' is:"
    )
    return generate_llm_response(change_output_prompt)