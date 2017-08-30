from random import SystemRandom
import data
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["POST", "OPTIONS"])
def generator():
    if request.method == "OPTIONS":
        return jsonify({})
    if request.method == "POST":
        data = request.get_json()
        program = data.get("major", "Software Engineering")
        language = data.get("language", "Java")
        colour = data.get("colour", "Blue")

        return jsonify(text=generate(program, language, colour))

def generate(program, language, colour):
    rand = SystemRandom()

    class_name = rand.choice(data.classes[program])
    first_name = rand.choice(data.first_names)
    title = rand.choice(data.titles)

    misc_skill = rand.choice(data.skills["Misc"])
    language_skill = rand.choice(data.skills[language])
    colour_skill = rand.choice(data.skills[colour])
    skill_nums = [rand.randint(-10, 10) for i in range(3)]
    skill_nums = [i if i < 0 else "+{}".format(i) for i in skill_nums]

    final = """
    {} {}, {}

    {} {}
    {} {}
    {} {}
    """.format(first_name, title, class_name,
               skill_nums[0], misc_skill,
               skill_nums[1], language_skill,
               skill_nums[2], colour_skill)

    print(final)
    print(final)
    print(final)
    print(final)

    return final


if __name__ == "__main__":
    character = generate("Computer Engineering", "Java", "Blue")
    app.run()
