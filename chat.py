# import required packages.
import os
import openai

openai.api_key = '<YOUR CHATGPT SECRET KEY>' #note that the key should be within environment or any other location  

# In this line we set the context for our chat-bot
messages = [
    { "role": "system", "content": "Sports management is one of the industries growing rapidly in Africa" }
]

while True:

    # An input field which alerts a user that they should input some data/message
    message = input("Ask me anything about sports: " )

    if message:
        messages.append(
            { "role": "user", "content": message }
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    response = chat.choices[0].message.content
    print(f"GPT response: {response}" )

    messages.append(
        { "role": "assistant", "content":response }
    )



