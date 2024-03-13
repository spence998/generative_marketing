LOCAL_MODEL = False

LOCAL_MODEL_PATH = r"C:\dev\mistral-7b-openorca.Q4_K_M\mistral-7b-openorca.Q4_K_M.gguf"
LOCAL_MODEL_TYPE = "mistral"

llm_parameters = {
    "temperature":0.8,
    "topK": 40,
}

campaign_options = [
    "Fraud",
    "Insurance",
    "International Payments",
]

content_size = {
    "Extra small": "less than 10 words",
    "Small": "between 10 and 20 words",
    "Medium": "between 20 and 40 words",
    "Large": "between 40 and 60 words",
    "Extra large": "more than 60 words",
}

business_size = [
    "Small",
    "Medium",
    "Large",
    "Any"
]

industry = [
    "Farming",
    "Any",
]