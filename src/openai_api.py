import openai
import os
import argparse

#create an argument parser
parser = argparse.ArgumentParser(description="OpenAI API")
parser.add_argument('--prompt', type=str, default='write a poem', help="Set the prompt for the API")
args = parser.parse_args()

# set the api key
openai.api_key = os.environ['OPENAI_API_KEY']
print(f"api key={openai.api_key}")
print(f"prompt is:{args.prompt}")

# creatfe a funciton ot call the openai api
def call_openai_api(prompt, engine="davinci", max_tokens=5):
    response = openai.Completion.create(
        engine = engine,
        prompt = prompt,
        max_tokens = max_tokens
    )
    return response

response = call_openai_api(args.prompt, max_tokens=100)
# print response text
print(response.choices[0].text)