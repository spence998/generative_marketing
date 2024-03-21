from flask import send_file

from app_file import app


@app.route('/download')
def downloadFile():
    path = "apps/gen_marketing/content_data/content_log.csv"
    return send_file(path, as_attachment=True)