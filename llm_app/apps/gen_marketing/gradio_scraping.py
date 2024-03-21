from gradio_client import Client


GRADIO_PATH = "https://0a7edb52fdab7135e0.gradio.live"


def get_gradio_model_response():

    client = Client(GRADIO_PATH, auth=("GENAIBCB", "GENAIBCBPWD"))
    result = client.predict("What is your name?", api_name="/predict")
    print(result)

get_gradio_model_response()