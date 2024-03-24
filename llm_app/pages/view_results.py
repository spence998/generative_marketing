from flask import  render_template, request, session


from app_file import app
from apps.gen_marketing.gen_marketing import change_llm_output
from apps.gen_marketing.utils import update_content_log


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
            session['product'],
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