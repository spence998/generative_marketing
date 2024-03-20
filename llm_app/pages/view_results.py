import pandas as pd
from flask import Flask, render_template, request, redirect, session, url_for, send_file
from apps.gen_marketing.gen_marketing import create_marketing_content, change_llm_output
from apps.gen_marketing.CONFIG import (
    campaign_options,
    content_size,
    business_size,
    industry,
)
from apps.gen_marketing.utils import get_all_records, update_content_log

from app_file import app


@app.route('/results', methods=['GET', 'POST'])
def view_results():
    content = session.get('content', None)
    if request.method == "POST":
        content[request.form["component"]] = change_llm_output(
            component=content[request.form["component"]],
            component_name=request.form["component"],
            change=request.form["request_headline_edit"],
        )
        session['content'] = content
        update_content_log(
            session['id'], 
            session['material_size'],
            content["headline"], 
            content["description"], 
            content["cta"],
        )

    return render_template(
        "generated_results.html", 
        headline=content["headline"],
        description=content["description"],
        cta=content["cta"],
    )