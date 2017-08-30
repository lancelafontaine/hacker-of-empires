from random import SystemRandom
import data
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def generator(request):
    program = request.form["major"]
    language = request.form["language"]
    colour = request.form["colour"]

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

    return final


# if __name__ == "__main__":
    
#     character = generate("Computer Engineering", "Java", "Blue")
#     print(character)
