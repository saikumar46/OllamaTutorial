import requests
import json
import gradio as gr
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type' : 'application/json',
}

history = []

def generate_response (prompt):
    history.append(prompt)
    final_prompt = "\n" .join(history)

    data = {

        "model" : "mistral",
        "prompt" : final_prompt ,
        "stream" : False
    }

    response = requests.post(url, headers = headers, data = json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_resonse = data['response']
        return actual_resonse
    
    else:
        print("Error:" , response.text)

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder ="Eneter your prompt"),
    outputs = "text"
)

interface.launch ()

