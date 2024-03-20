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


@app.route('/download')
def downloadFile():
    path = "apps/gen_marketing/content_data/content_log.csv"
    return send_file(path, as_attachment=True)