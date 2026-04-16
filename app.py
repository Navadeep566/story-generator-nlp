from flask import Flask, render_template, request, jsonify
from groq import Groq
import time

app = Flask(__name__)

# Paste your Groq API Key
client = Groq(api_key="YOUR_API_KEY")


def generate_story(data):

    genre = data["genre"]
    mood = data["mood"]
    character_name = data["character_name"]
    character_role = data["character_role"]
    setting = data["setting"]
    goal = data["goal"]
    conflict = data["conflict"]
    ending_type = data["ending_type"]
    plot_twist = data["plot_twist"]
    story_length = data["story_length"]

    if story_length.lower() == "short":
        length_rule = "Write around 150 words."
    elif story_length.lower() == "medium":
        length_rule = "Write around 300 words."
    else:
        length_rule = "Write around 600 words."

    prompt = f"""
Generate a creative story based on these user inputs.

Genre: {genre}
Mood: {mood}
Character Name: {character_name}
Character Role: {character_role}
Setting: {setting}
Goal: {goal}
Conflict: {conflict}
Ending Type: {ending_type}
Plot Twist: {plot_twist}

Rules:
1. Story must match genre.
2. Mood controls tone.
3. Use all user inputs clearly.
4. {length_rule}

Give output exactly:

Title:
<Title>

Story:
<Story>

Summary:
<Summary>
"""

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=1,
                max_tokens=2200
            )

            return response.choices[0].message.content

        except:
            time.sleep(2)

    return "Error generating story."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    result = generate_story(data)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)