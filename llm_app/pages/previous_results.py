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


@app.route('/previous-results', methods=['GET', 'POST'])
def previous_results():
    content_log = get_all_records()
    print(request.form)

    if request.method == "POST":
        id_filter = request.form["id_filter"],
        content_size_filter = request.form["content_size_filter"],
        date_from_filter = request.form["date_from_filter"],
        date_to_filter = request.form["date_to_filter"],
        
        if id_filter[0] == "":
            id_filter = pd.Series([True]*content_log.shape[0])
        else:
            id_filter = (content_log["ID"] == id_filter[0])

        if content_size_filter[0] == "":
            content_size_filter = pd.Series([True]*content_log.shape[0])
        else:
            content_size_filter = (content_log["Content Size"] == content_size_filter[0])

        if date_from_filter[0] == "":
            date_from_filter = pd.Series([True]*content_log.shape[0])
        else:
            date_from_filter = (content_log["Datetime"] >= date_from_filter[0])

        if date_to_filter[0] == "":
            date_to_filter = pd.Series([True]*content_log.shape[0])
        else:
            date_to_filter = (content_log["Datetime"] <= date_to_filter[0])
        
        data_filter = (
            id_filter & content_size_filter & date_from_filter & date_to_filter
        )

        print(data_filter)

        content_log = content_log[data_filter]

    return render_template(
            "content_log.html",
            table=content_log.to_html(classes='data', header="true")
        )