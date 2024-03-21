LOCAL_MODEL = False
GRADIO_MODEL = True

LOCAL_MODEL_PATH = r"C:\dev\mistral-7b-openorca.Q4_K_M\mistral-7b-openorca.Q4_K_M.gguf"
LOCAL_MODEL_TYPE = "mistral"

llm_parameters = {
    "temperature":0.8,
    "topK": 40,
}

campaign_options = {
    "Asset Finance": "business asset finance",
    "Biometric Security Feature": "biometric security feature",
    "Address Change Reminder": "business address change reminder",
    "Charge Cards": "business charge cards",
    "Credit and Charge Cards": "business credit and charge cards",
    "Credit Cards": "business credit cards",
    "Current Account": "business current account",
    "Financial Assistant ": "business financial assistant ",
    "Fraud": "business fraud",
    "Insurance": "business insurance",
    "Invoice Finance": "business invoice finance",
    "Loans": "business loans",
    "Online Banking": "business online banking",
    "Overdraft": "business overdraft",
    "Payments Management": "business payments management",
    "Savings Accounts": "business savings accounts",
    "Cardnet": "cardnet",
    "Cheque Deposits": "cheque deposits",
    "International Business Payments on the Mobile App": "international business payments from the mobile app",
    "International Business Payments": "international business payments",
    "Mobile App Features": "mobile app features",
    "Online Business Banking": "online business banking",
    "Paperless Business Banking Statements": "paperless business banking statements",
    "Password Reset": "password reset",
    "Upcoming Outage": "Upcoming outage",
    "Virtual Assistant": "virtual assistant",
}

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