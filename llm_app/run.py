from flask import Flask, render_template, request, redirect, session, url_for
from apps.gen_marketing.gen_marketing import create_marketing_content, change_llm_output
from apps.gen_marketing.CONFIG import (
    campaign_options,
    content_size,
    business_size,
    industry,
)


app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = create_marketing_content(
            topic=request.form["topic"],
            material_size=request.form["material_size"],
            business_size=request.form["business_size"],
            industry=request.form["industry"],
            aim=request.form["aim"],
        )
        session['content'] = content
        return redirect(url_for('view_results'))
    
    else:
        return render_template(
            "marketing_form.html",
            campaign_options=campaign_options,
            content_size=content_size.keys(),
            business_size=business_size,
            industry=industry,
        )


@app.route('/results', methods=['GET', 'POST'])
def view_results():
    content = session.get('content', None)
    if request.method == "POST":
        content[request.form["component"]] = change_llm_output(
            component=content[request.form["component"]],
            component_name=request.form["component"],
            change=request.form["request_headline_edit"],
        )
    return render_template(
        "generated_results.html", 
        headline=content["headline"],
        description=content["description"],
        cta=content["cta"],
    )



if __name__=="__main__":
    app.run()
