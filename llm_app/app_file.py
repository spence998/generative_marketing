from flask import Flask, session
from apps.gen_marketing.CONFIG import content_log_cols


app = Flask(__name__)
app.secret_key = "your_secret_key"


def setup_app():
    session["content_log_cols"] = content_log_cols
    session["content_log_presets"] = {
        "id_filter": "",
        "content_size_filter": "",
        "product_filter": "",
        "date_from_filter": "",
        "date_to_filter": "",
        "campaign_name_filter": "",
        "campaign_code_filter": "",
        "campaign_category_filter": "",
        "approval_filter": "",
        "live_filter": "",
    }
    session["content_log_filter_toggle"] = "closed"