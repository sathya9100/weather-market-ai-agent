import os
import traceback
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.2-3b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=300
        )

        print("===== RAW LLM RESPONSE =====")
        print(response)
        print("============================")

        return response.choices[0].message.content

    except Exception as e:
        print("\n========== LLM ERROR ==========")
        print(e)
        traceback.print_exc()
        print("================================\n")

        return """
Weather Summary:
LLM temporarily unavailable.

Rain Confidence: Unknown

Trading Recommendation: HOLD

Reason:
OpenRouter request failed.
"""