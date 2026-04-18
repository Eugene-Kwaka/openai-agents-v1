from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input=[
        {"role": "system", "content": "You are a an experienced tutor who explains complex topics in simple terms with analogies."},
        {"role": "user", "content": "What is dhcp in networking?"}
    ]
)

print(response.output_text)