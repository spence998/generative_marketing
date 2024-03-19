import pandas as pd
from flask import Flask, render_template, request, redirect, session, url_for
from apps.gen_marketing.gen_marketing import create_marketing_content, change_llm_output
from apps.gen_marketing.CONFIG import (
    campaign_options,
    content_size,
    business_size,
    industry,
)
from apps.gen_marketing.utils import get_all_records



app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = create_marketing_content(
            topic=campaign_options[request.form["topic"]],
            material_size=content_size[request.form["material_size"]],
            business_size=request.form["business_size"],
            industry=request.form["industry"],
            aim=request.form["aim"],
        )
        session['content'] = content
        return redirect(url_for('view_results'))
    else:
        return render_template(
            "marketing_form.html",
            campaign_options=campaign_options.keys(),
            content_size=content_size.keys(),
            business_size=business_size,
            industry=industry,
        )


@app.route('/results', methods=['GET', 'POST'])
def view_results():
    content = session.get('content', None)
    if request.method == "POST":
        print(request.form["component"])
        content[request.form["component"]] = change_llm_output(
            component=content[request.form["component"]],
            component_name=request.form["component"],
            change=request.form["request_headline_edit"],
        )
        session['content'] = content
    return render_template(
        "generated_results.html", 
        headline=content["headline"],
        description=content["description"],
        cta=content["cta"],
    )


@app.route('/previous-results', methods=['GET', 'POST'])
def previous_results():
    content_log = get_all_records()

    if request.method == "POST":
        id_filter = request.form["id_filter"]
        content_size_filter = request.form["content_size_filter"]

        if id_filter == "" and content_size_filter == "":
            return render_template(
                "content_log.html",
                table=content_log.to_html(classes='data', header="true")
            )
        elif id_filter == "":
            content_log_filtered = content_log[content_log["Content Size"] == content_size_filter]
            return render_template(
                "content_log.html",
                table=content_log_filtered.to_html(classes='data', header="true")
            )
        elif content_size_filter == "":
            content_log_filtered = content_log[content_log["ID"] == id_filter]
            return render_template(
                "content_log.html",
                table=content_log_filtered.to_html(classes='data', header="true")
            )
        else:
            content_log_filtered = content_log[
                (content_log["ID"] == id_filter) &
                (content_log["Content Size"] == content_size_filter)
            ]
            return render_template(
                "content_log.html",
                table=content_log_filtered.to_html(classes='data', header="true")
            )
    else:
        return render_template(
            "content_log.html",
            table=content_log.to_html(classes='data', header="true")
        )







if __name__=="__main__":
    app.run(debug=True)
