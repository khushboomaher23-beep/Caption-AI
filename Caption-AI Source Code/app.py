import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_production_secret_key_2026")

api_key = os.getenv("GROQ_API_KEY")
groq_client = None

if api_key and "actual" not in api_key:
    groq_client = Groq(api_key=api_key)

def generate_marketing_assets(description, platform, tone):
    if not groq_client:
        return "❌ [CONFIGURATION ERROR] Missing valid Groq API Key inside your .env file."

    # Prompt updated to strictly demand high engagement emojis based on platform
    system_prompt = (
        "You are an expert elite copywriter and social media growth strategist. "
        "You integrate highly relevant, trendy emojis natively throughout your responses to maximize conversion."
    )

    user_prompt = f"""
    Context/Product: {description}
    Target Platform: {platform}
    Brand Voice Tone: {tone}

    Execution Deliverables:
    1. [CAPTIONS]: Create exactly 3 dynamic, high-engagement variations custom targeted to {platform} using a {tone} tone. You MUST embed vibrant, context-specific emojis at the start, middle, and end of each caption variation to bring it alive.
    2. [HASHTAGS]: Compile exactly 10 optimized tags separated by spaces.
    3. [CTAS]: Formulate exactly 3 distinct high-converting target Call to Actions with active behavioral triggers and urgency emojis.

    Format output cleanly as:
    [CAPTIONS]
    1. (Insert Variation One with rich emojis)
    2. (Insert Variation Two with rich emojis)
    3. (Insert Variation Three with rich emojis)

    [HASHTAGS]
    #tag1 #tag2 #tag3 ...

    [CTAS]
    1. (Action CTA One 🚀)
    2. (Action CTA Two ✨)
    3. (Action CTA Three 🔗)
    """

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8, # Slightly increased for high creativity & emoji richness
            max_tokens=1200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ [PIPELINE RUNTIME ERROR] Groq Cloud API Engine rejected handshake: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def dashboard_endpoint():
    if request.method == 'POST':
        description = request.form.get('description', '').strip()
        platform = request.form.get('platform', '')
        tone = request.form.get('tone', '')
        raw_output = generate_marketing_assets(description, platform, tone)
        return render_template('index.html', raw_output=raw_output, description=description, platform=platform, tone=tone)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)