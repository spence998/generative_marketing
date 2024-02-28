from flask import Flask, render_template, request
from apps.gen_marketing.gen_marketing import null_func
from apps.gen_marketing.CONFIG import (
    campaign_options,
    content_size,
    business_size,
)


app = Flask(__name__)


def example_fnc():
    print("Function is working")

from flask import *
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        topic_dropdown = request.form["topic_dropdown"]
        other_details = request.form["other_details"]
        null_func()
        return render_template(
            "result.html", 
            topic=topic,
            topic_dropdown=topic_dropdown,
            other_details=other_details,
        )
    else:
        return render_template(
            "marketing_form.html",
            campaign_options=campaign_options,
            content_size=content_size,
            business_size=business_size,
        )


if __name__=="__main__":
    app.run(debug=True)