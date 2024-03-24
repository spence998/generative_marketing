import pandas as pd
from datetime import datetime


def update_content_log(
    id_name,
    product,
    content_size,
    headline,
    main_content,
    cta,
):
    try:
        df = pd.read_csv("apps/gen_marketing/content_data/content_log.csv")
    except:
        df = pd.DataFrame(
            {
                "ID / Name":[],
                "Product": [],
                "Datetime": [],
                "Content Size": [],
                "Headline": [],
                "Main content": [],
                "CTA": [],
            }
        )
    if id_name == "":
        id_name = "Missing"
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                {
                    "ID / Name": [id_name],
                    "Product": [product],
                    "Datetime": [str(datetime.now())[:-10]],
                    "Content Size": [content_size],
                    "Headline": [headline],
                    "Main content": [main_content],
                    "CTA": [cta],
                }
            )
        ]
    )
    df.to_csv(
        "apps/gen_marketing/content_data/content_log.csv",
        index=None
    )


def filter_records(id_filter, content_size):
    marketing_content_data = pd.read_csv("apps/gen_marketing/content_data/content_log.csv")
    id_filter = marketing_content_data["ID"] == id_filter
    content_filter = marketing_content_data["Content Size"] == content_size
    
    data_filter = (id_filter & content_filter)  
    
    return marketing_content_data[data_filter]


def get_all_records():
    content_log = pd.read_csv("apps/gen_marketing/content_data/content_log.csv")
    content_log["Datetime"] = pd.to_datetime(
        content_log["Datetime"],
        format='%Y-%m-%d %H:%M',
    )
    return content_log


def remove_quote_marks(string):
    while string[0] in ["\'", '\"', " ", r"\\"]:
        string = string[1:]
    while string[-1] in ["\'", '\"', " ", r"\\"]:
        string = string[:-1]
    return string