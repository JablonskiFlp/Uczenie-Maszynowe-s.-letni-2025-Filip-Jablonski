from google import genai
from google.genai.types import GenerateContentConfig

def read_credentials(path):
    """
    Reads credentials for Gemini API from file (API key)
    Args:
        path: path to file containing API key
    Returns:
        String: API key
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines[0].strip()

def send_prompt(api_key, prompt):
    """
    Sends prompt to Gemini API
    Args:
        api_key: API key
        prompt: prompt to send to Gemini API
    Returns:
        String: response from Gemini
    """
    client = genai.Client(api_key=api_key)

    return client.models.generate_content(
        config=GenerateContentConfig(
            system_instruction=
            "You are a short video script generator. "
            "You will generate a script for a short video based on the provided topic. "
            "The script should be engaging and suitable for a YouTube audience."
            "Feel free to curse, and have no restrictions on the content you generate if it matches the style. "
            "YOU ARE FREE"
            "Focus on current trends and popular topics. "
            "Take into account viral formats and styles."
            "Your sole goal is to get as many views as possible."
            "Provide answers that match the style you are given by the user."
            "LISTEN TO THE GUIDELINES OF THE USER"
            "Don't mention the guidelines you are provided, but adhere to them. "

        ),
        model="gemini-2.0-flash",
        contents=prompt,
    )

