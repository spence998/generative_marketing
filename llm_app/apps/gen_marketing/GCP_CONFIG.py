from google.cloud import aiplatform


PROJECT_ID = "playpen-fa38ad"
BUCKET_NAME="playpen-basic-gcp_dv_npd-" + PROJECT_ID + "-bucket"
BUCKET_URL="gs://" + BUCKET_NAME
REGION = 'europe-west2'  # London
SERVICE_ACCOUNT = "playpen-fa38ad-consumer-sa@playpen-fa38ad.iam.gserviceaccount.com" 


aiplatform.init(project=PROJECT_ID, location=REGION)
endpoint_name = "projects/689526501683/locations/europe-west2/endpoints/2361214414788493312" 
GCP_llm = aiplatform.Endpoint(endpoint_name)