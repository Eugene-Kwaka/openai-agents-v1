from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="Write a one-sentence story about AI."
)

print(response.output_text)