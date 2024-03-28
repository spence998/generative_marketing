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
            session['content_inputs']['id_name'],
            session['content_inputs']['campaign_name'],
            session['content_inputs']['campaign_code'],
            session['content_inputs']['campaign_category'],
            session['content_inputs']['product'],
            session['content_inputs']['content_size'],
            session['content']["headline"], 
            session['content']["description"], 
            session['content']["cta"],
        )

    return render_template(
        "generated_results.html", 
        marketing_content=session["content"],
    )