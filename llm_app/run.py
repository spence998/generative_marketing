from flask import render_template, request, redirect, session, url_for

from app_file import app, setup_app
from apps.gen_marketing.CONFIG import (
    business_size,
    campaign_options,
    content_size,
    industry,
)
from apps.gen_marketing.gen_marketing import create_marketing_content
from apps.gen_marketing.utils import update_content_log

from pages import (
    previous_results,
    view_results,
)


@app.route("/", methods=["GET", "POST"])
def index():
    setup_app()

    if request.method == "POST":
        session['content'] = create_marketing_content(
            product=campaign_options[request.form["product"]],
            material_size=content_size[request.form["content_size"]],
            business_size=request.form["business_size"],
            industry=request.form["industry"],
            aim=request.form["aim"],
        )
        session['content_inputs'] = {
            "id_name": request.form["id_name"],
            "campaign_name": request.form["campaign_name"],
            "campaign_code": request.form["campaign_code"],
            "campaign_category": request.form["campaign_category"],
            "product": request.form["product"],
            "content_size": request.form["content_size"],
            "business_size": request.form["business_size"],
            "industry": request.form["industry"],
            "aim": request.form["aim"],
        }
        update_content_log(
            session['content_inputs']['id_name'],
            session['content_inputs']['campaign_name'],
            session['content_inputs']['campaign_code'],
            session['content_inputs']['campaign_category'],
            session['content_inputs']['product'],
            session['content_inputs']['content_size'],
            session["content"]["headline"], 
            session["content"]["description"], 
            session["content"]["cta"],
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
