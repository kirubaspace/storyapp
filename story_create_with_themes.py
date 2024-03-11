from openai import OpenAI
import os

# Setup
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url='https://api.together.xyz/v1',
)

# New feature to generate a short story based on an array of themes
themes = ["tamil", "nature", "charlie munger", "god help", "grandfather"]

# Formatting the array of themes into a string that the AI can understand
themes_prompt = "Create a short story that includes the following themes: " + ", ".join(themes) + ". The story should be engaging and concise, ideally less than one page."

# Generating the short story
chat_completion_story = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": themes_prompt,
        },
        {
            "role": "user",
            "content": "Please start the story now.",
        }
    ],
    model="mistralai/Mixtral-8x7B-Instruct-v0.1"
)

# Output the generated story
print(chat_completion_story.choices[0].message.content)

