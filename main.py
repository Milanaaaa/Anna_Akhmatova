import json

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list_sources")
def list_sources():
    return render_template("list_sources.html")


@app.route("/author_page")
def author_page():
    return render_template("author_page.html")


@app.route("/biography")
def biography():
    return render_template("biography.html")


@app.route("/creativity")
def creativity():
    return render_template("creativity.html")


@app.route("/poems")
def poems():
    with open('templates/poems.json', encoding="utf-8") as file:
        list_poems = json.load(file)
    return render_template("poems.html", list_poems=list_poems)


@app.route("/poem_page/<int:id>")
def poem_page(id):
    with open('templates/poems.json', encoding="utf-8") as file:
        list_poems = json.load(file)
    for p in list_poems:
        if p['id'] == id:
            title = p['title']
            date = p['date']
            text = p['text']
    return render_template("poem_page.html", title=title, date=date, text=text)


@app.route("/facts")
def facts():
    colors = ['alert alert-danger', 'alert alert-warning', 'alert alert-success', 'alert alert-info',
              'alert alert-primary']
    with open('templates/facts.json', encoding="utf-8") as file:
        list_facts = json.load(file)
    return render_template("facts.html", list_facts=list_facts, colors=colors)


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
