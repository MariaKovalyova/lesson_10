from utils import get_person

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return get_person()


@app.route('/candidates/<id_candidate>')
def candidates(id_candidate):
    return get_person(id_candidate)


@app.route('/skills/<skill>')
def skills(skill):
    return get_person(skill)


app.run()