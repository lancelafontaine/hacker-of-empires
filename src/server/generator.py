from random import SystemRandom
import data
from flask import Flask, jsonify, request
from flask_cors import CORS

allowed_hosts = [
    'http://localhost:8080',
    'https://empires.scsconcordia.com'
]

app = Flask(__name__)
CORS(app, origins=allowed_hosts)


@app.route('/', methods=["POST", "OPTIONS"])
def generator():
    if request.method != "POST":
        return jsonify({})

    data = request.get_json()
    program = data.get("major", "soen").strip().lower()
    language = data.get("language", "java").strip().lower()
    colour = data.get("colour", "blue").strip().lower()

    return jsonify(text=generate(program, language, colour))


def generate(program, language, colour):
    rand = SystemRandom()

    skill_nums = [str(i) if i < 0 else "+{}".format(i) for i in range(-10, 11)]
    skill_nums.remove("+0")

    response_data = {
        "first_name": rand.choice(data.first_names),
        "title": rand.choice(data.titles),
        "class_name": rand.choice(data.classes[program]),
        "misc_skill": {
            "number": rand.choice(skill_nums),
            "skill": rand.choice(data.skills["misc"])
        },
        "language_skill": {
            "number": rand.choice(skill_nums),
            "skill": rand.choice(data.skills[language])
        },
        "colour_skill": {
            "number": rand.choice(skill_nums),
            "skill": rand.choice(data.skills[colour])
        }
    }

    return response_data

if __name__ == "__main__":
    app.run()
