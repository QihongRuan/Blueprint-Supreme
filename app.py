import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- CONFIGURATION ---
# IMPORTANT: Replace "YOUR_GEMINI_API_KEY" with your actual Gemini API key.
# You can get your key from Google's AI Studio.
# It's recommended to set this as an environment variable for security.
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    # If the environment variable is not set, use a placeholder.
    # The app will not work until this is replaced with a real key.
    print("WARNING: GEMINI_API_KEY environment variable not found.")
    print("Please set it or replace the placeholder in the code.")
    genai.configure(api_key="YOUR_GEMINI_API_KEY")


# --- RAP GENERATION LOGIC ---
def generate_rap_verse(keywords):
    """Generates a rap verse using the Gemini API."""

    model = genai.GenerativeModel('gemini-pro')

    # The original rap song to provide context and style
    original_rap = """
    (Intro)
    Yeah, Super Bowl in the house, 超级碗 in the building
    Gemini 3 SuperHack, we about to make a killin'
    From the Middle Kingdom to the City of Angels
    This is for the dreamers, time to spread your wings, let's go!

    (Chorus)
    大展鸿图, yeah, we on a mission
    Super Bowl dreams, fueled by ambition
    From the East to the West, we share the same fire
    To be a champion, take it higher and higher
    大展鸿图, spread your wings and fly
    Touchdown in your life, reach for the sky
    This ain't just a game, it's a story to be told
    Of how we chase our dreams, more precious than gold
    """

    # The prompt for the AI model
    prompt = f"""
    You are a creative rap artist. You are competing in the Gemini 3 SuperHack.
    Your style is a mix of English and Chinese, and your theme is "大展鸿图" (realizing grand ambitions).
    You have already written a rap song, which is provided below as a style reference:

    ---
    {original_rap}
    ---

    Now, create a new, short rap verse (about 4-6 lines) in the same style.
    This new verse must be inspired by the following keywords: "{keywords}".
    Make it energetic, confident, and inspiring.
    Make sure to continue the theme of ambition and success.
    Do not repeat the chorus.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating rap verse: {e}")
        return "Oops! The AI is taking a timeout. Please try again."


# --- ROUTES ---
@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """API endpoint to generate a rap verse."""
    data = request.get_json()
    keywords = data.get('keywords')

    if not keywords:
        return jsonify({'error': 'Keywords are required.'}), 400

    verse = generate_rap_verse(keywords)
    return jsonify({'verse': verse})


if __name__ == '__main__':
    app.run(debug=True)
