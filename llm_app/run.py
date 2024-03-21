from flask import render_template, request, redirect, session, url_for

from app_file import app
from apps.gen_marketing.CONFIG import (
    business_size,
    campaign_options,
    content_size,
    industry,
)
from apps.gen_marketing.gen_marketing import create_marketing_content
from apps.gen_marketing.utils import update_content_log



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = create_marketing_content(
            product=campaign_options[request.form["product"]],
            material_size=content_size[request.form["material_size"]],
            business_size=request.form["business_size"],
            industry=request.form["industry"],
            aim=request.form["aim"],
        )
        session['content'] = content
        session['id'] = request.form["id_name"]
        session['product'] = request.form["product"]
        session['material_size'] = request.form["material_size"]
        update_content_log(
            session['id'],
            session['product'],
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
