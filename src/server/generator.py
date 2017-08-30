from random import SystemRandom
import data
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["POST", "OPTIONS"])
def generator():
    if request.method != "POST":
        return jsonify({})

    data = request.get_json()
    program = data.get("major", "soen")
    language = data.get("language", "java")
    colour = data.get("colour", "blue")

    return jsonify(text=generate(program, language, colour))

def generate(program, language, colour):
    rand = SystemRandom()

    skill_nums = [str(i) if i < 0 else "+{}".format(i) for i in range(-10, 11)]
    skill_nums.remove("+0")

    skills = [
        "{} {}".format(rand.choice(skill_nums), rand.choice(data.skills["misc"])),
        "{} {}".format(rand.choice(skill_nums), rand.choice(data.skills[language])),
        "{} {}".format(rand.choice(skill_nums), rand.choice(data.skills[colour]))
    ]

    name = "{} {}, {}".format(rand.choice(data.first_names), rand.choice(data.titles), rand.choice(data.classes[program]))

    final = """
    {}

    {}
    {}
    {}
    """.format(name, *skills)

    return final

if __name__ == "__main__":
    app.run()
