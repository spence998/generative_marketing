import pandas as pd
from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for,
    send_file,
    jsonify,
)

from app_file import app, setup_app
from apps.gen_marketing.utils import get_all_records
 

@app.route('/content_log', methods=['GET', 'POST'])
def previous_results():
    if "content_log_presets" not in session.keys():
        setup_app()
        
    content_log = get_all_records()
    all_content_log_cols=content_log.columns
    request_form_dict = dict(request.form.lists())  

    if request.method == "POST" and request_form_dict.keys().__contains__("content_log_cols"):
        session["content_log_cols"] = request_form_dict["content_log_cols"]

    if request.method == "POST" and not request_form_dict.keys().__contains__("content_log_cols"):
        session["content_log_presets"] = {
            "id_filter": request.form["id_filter"],
            "content_size_filter": request.form["content_size_filter"],
            "product_filter": request.form["product_filter"],
            "date_from_filter": request.form["date_from_filter"],
            "date_to_filter": request.form["date_to_filter"],
            "campaign_name_filter": request.form["campaign_name_filter"],
            "campaign_code_filter": request.form["campaign_code_filter"],
            "campaign_category_filter": request.form["campaign_category_filter"],
            "approval_filter": request.form["approval_filter"],
            "live_filter": request.form["live_filter"],
        }


        if request.form["id_filter"] == "":
            id_filter = pd.Series([True]*content_log.shape[0])
        else:
            id_filter = (content_log["ID / Name"] == request.form["id_filter"])
        
        if request.form["content_size_filter"] == "":
            content_size_filter = pd.Series([True]*content_log.shape[0])
        else:
            content_size_filter = (content_log["Content Size"] == request.form["content_size_filter"])

        if request.form["product_filter"] == "":
            product_filter = pd.Series([True]*content_log.shape[0])
        else:
            product_filter = (content_log["Product"] == request.form["product_filter"])

        if request.form["date_from_filter"] == "":
            date_from_filter = pd.Series([True]*content_log.shape[0])
        else:
            date_from_filter = (content_log["Datetime"] >= request.form["date_from_filter"])

        if request.form["date_to_filter"] == "":
            date_to_filter = pd.Series([True]*content_log.shape[0])
        else:
            date_to_filter = (content_log["Datetime"] - pd.DateOffset(1) <= request.form["date_to_filter"])

        if request.form["campaign_name_filter"] == "":
            campaign_name_filter = pd.Series([True]*content_log.shape[0])
        else:
            campaign_name_filter = (content_log["Campaign name"] == request.form["campaign_name_filter"])

        if request.form["campaign_code_filter"] == "":
            campaign_code_filter = pd.Series([True]*content_log.shape[0])
        else:
            campaign_code_filter = (content_log["Campaign code"] == request.form["campaign_code_filter"])

        if request.form["campaign_category_filter"] == "":
            campaign_category_filter = pd.Series([True]*content_log.shape[0])
        else:
            campaign_category_filter = (content_log["Campaign category"] == request.form["campaign_category_filter"])
        
        if request.form["approval_filter"] == "Any":
            approval_filter = pd.Series([True]*content_log.shape[0])
        else:
            approval_filter = (content_log["Approved"] == request.form["approval_filter"])

        if request.form["live_filter"] == "Any":
            live_filter = pd.Series([True]*content_log.shape[0])
        else:
            live_filter = (content_log["Live"] == request.form["live_filter"])
        

        data_filter = (
            id_filter & 
            product_filter &
            content_size_filter & 
            date_from_filter & 
            date_to_filter &
            campaign_name_filter &
            campaign_code_filter &
            campaign_category_filter &
            approval_filter &
            live_filter 
        )
        content_log = content_log[data_filter]

    content_log_cols = session["content_log_cols"]
    content_log = content_log[content_log_cols]

    return render_template(
        "content_log.html",
        table=content_log.to_html(classes='data', header="true"),
        all_content_log_cols=all_content_log_cols,
        selected_cols=content_log_cols,
        content_log_presets=session["content_log_presets"],
        toggle_filter=session["content_log_filter_toggle"],
    )


@app.route('/content_log/reset_presets')
def reset_presets():
    session["content_log_presets"] = {
        "id_filter": "",
        "product_filter": "",
        "content_size_filter": "",
        "date_from_filter": "",
        "date_to_filter": "",
        "campaign_name_filter": "",
        "campaign_code_filter": "",
        "campaign_category_filter": "",
        "approval_filter": "",
        "live_filter": ""
    }
    return redirect(url_for('previous_results'))


@app.route('/content_log/download')
def download_file():
    path = "apps/gen_marketing/content_data/content_log.csv"
    return send_file(path, as_attachment=True)


@app.route('/content_log/toggle_filter', methods=['POST'])
def toggle_filter():
    data = request.data.decode('utf-8')
    session["content_log_filter_toggle"] = data
    return 'Data received successfully', 200
