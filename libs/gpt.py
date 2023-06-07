import openai
import env


openai.api_key = env.load("OPENAI.APIKEY")
ans = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(ans)
# gpt-3.5-turbo	$0.002 / 1000 tokens
# 1USD for 500,000 tokens