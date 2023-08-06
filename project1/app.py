import openai
import gradio
import time

# Set your OpenAI API key here
openai.api_key = "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"

# Initialize conversation history with system message
messages = [{"role": "system",
             "content": "You are a financial expert specializing in real estate investment and negotiation."}]


def CustomChatGPT(user_input):
    # Append user message to conversation history
    messages.append({"role": "user", "content": user_input})

    # Wait for a short period to avoid hitting the rate limit
    time.sleep(2)

    # Make API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract assistant's reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # Append assistant's reply to conversation history
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply


# Create the Gradio interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the Gradio web app
demo.launch(share=True)
