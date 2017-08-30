from random import SystemRandom
import data
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

allowed_hosts = [
    'http://localhost:8080',
    'https://empires.scsconcordia.com'
]

app = Flask(__name__)
CORS(app, origins=allowed_hosts)

@app.route('/', methods=["POST", "OPTIONS"])
def generator():
    if request.method == "OPTIONS":
        return jsonify({})
    if request.method == "POST":
        data = request.get_json()
        program = data.get("major", "soen").strip().lower()
        language = data.get("language", "java").strip().lower()
        colour = data.get("colour", "blue").strip().lower()
        email = data.get("email", "fake@fake.fake").strip().lower()

        save_to_db(program, language, colour, email)

        return jsonify(text=generate(program, language, colour))

def generate(program, language, colour):
    rand = SystemRandom()

    class_name = rand.choice(data.classes[program])
    first_name = rand.choice(data.first_names)
    title = rand.choice(data.titles)

    misc_skill = rand.choice(data.skills["misc"])
    language_skill = rand.choice(data.skills[language])
    colour_skill = rand.choice(data.skills[colour])
    skill_nums = [rand.randint(-10, 10) for i in range(3)]
    skill_nums = [i if i < 0 else "+{}".format(i) for i in skill_nums]

    response_data = {
        "first_name": first_name,
        "title": title,
        "class_name": class_name,
        "misc_skill": {
            "number": str(skill_nums[0]),
            "skill": misc_skill
        },
        "language_skill": {
            "number": str(skill_nums[1]),
            "skill": language_skill
        },
        "colour_skill": {
            "number": str(skill_nums[2]),
            "skill": colour_skill
        }
    }

    return response_data

def save_to_db(program, language, colour, email):
    connection = sqlite3.connect('example.db')
    c = connection.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS hackers (program text, language text, colour text, email text)')
    c.execute('INSERT INTO hackers VALUES (?,?,?,?)', (program, language, colour, email))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    app.run()
