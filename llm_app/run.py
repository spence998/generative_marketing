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
from pages import (
    downloadFile,
    previous_results,
    view_results,
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = create_marketing_content(
            topic=campaign_options[request.form["product"]],
            material_size=content_size[request.form["material_size"]],
            business_size=request.form["business_size"],
            industry=request.form["industry"],
            aim=request.form["aim"],
        )
        session['content'] = content
        session['id'] = request.form["id_name"]
        session['material_size'] = request.form["material_size"]
        update_content_log(
            session['id'], 
            session['material_size'],
            content["headline"], 
            content["description"], 
            content["cta"],
        )
        return redirect(url_for('view_results'))
    else:
        return render_template(
            "marketing_form.html",
            campaign_options=campaign_options.keys(),
            content_size=content_size.keys(),
            business_size=business_size,
            industry=industry,
        )


if __name__=="__main__":
    app.run(debug=True)
