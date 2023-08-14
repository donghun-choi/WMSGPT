import openai
from libs import env


openai.api_key = str(env.load('OPENAI.APIKEY'))

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "야!"}]
)

print(response.choices[0].message.content)