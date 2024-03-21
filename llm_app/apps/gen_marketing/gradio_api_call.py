from gradio_client import Client


GRADIO_PATH = "https://0a7edb52fdab7135e0.gradio.live"


def get_gradio_model_response(prompt):
    client = Client(GRADIO_PATH, auth=("GENAIBCB", "GENAIBCBPWD"))
    result = client.predict(prompt, api_name="/predict")
    return result

if __name__=="__main__":
    get_gradio_model_response("What is your name?")
