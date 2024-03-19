LOCAL_MODEL = True

LOCAL_MODEL_PATH = r"C:\dev\mistral-7b-openorca.Q4_K_M\mistral-7b-openorca.Q4_K_M.gguf"
LOCAL_MODEL_TYPE = "mistral"

llm_parameters = {
    "temperature":0.8,
    "topK": 40,
}

campaign_options = {
    "Asset Finance": "business asset finance",
    "Biometric Security Feature": "biometric security feature",
    "Business Address Change Reminder": "business address change reminder",
    "Business Asset Finance": "business asset finance",
    "Business Charge Cards": "business charge cards",
    "Business Credit and Charge Cards": "business credit and charge cards",
    "Business Credit Cards": "business credit cards",
    "Business Current Account": "business current account",
    "Business Financial Assistant ": "business financial assistant ",
    "Business Fraud": "business fraud",
    "Business Insurance": "business insurance",
    "Business Invoice Finance": "business invoice finance",
    "Business Loans": "business loans",
    "Business Online Banking": "business online banking",
    "Business Overdraft": "business overdraft",
    "Business Payments Management": "business payments management",
    "Business Savings Accounts": "business savings accounts",
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