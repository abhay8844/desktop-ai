import openai

openai.api_key = "your-secret-api-key"

def get_response_from_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" or others depending on your needs.
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

user_input = input("User: ")
response = get_response_from_gpt(user_input)
print("Assistant:", response)
